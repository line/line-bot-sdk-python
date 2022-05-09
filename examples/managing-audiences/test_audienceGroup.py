# -*- coding: utf-8 -*-
import logging
from linebot import LineBotApi as LineBotApi_ori

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M',
    handlers=[logging.FileHandler('my.log', 'w', 'utf-8'), ]
)

channel_access_token = 'xxxxxxx'

tester = [
    "Utesttestesttesttesttestestest18",
    "Utesttestesttesttesttestestest61",
    "Utesttestesttesttesttestestest59",
    "Utesttestesttesttesttestestest89",
    "Utesttestesttesttesttestestest79",
    "Utesttestesttesttesttestestest8c",
    "Utesttestesttesttesttestestestc3",
    "Utesttestesttesttesttestestest29",
    "Utesttestesttesttesttestestest03",
]

line_ids = {
    "tester": tester,
    "tester1": tester[:5],
    "測試": tester[:4],
    "tester2": tester[:3],
    "tester3": tester[:2],
    "tester john": tester[:1],
}

request_id = "xxxxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx"


class LineBotApi(LineBotApi_ori):
    def create_audience_group(self, audience_group_name, audiences,
                              is_ifa=False, mode="normal", timeout=None):
        if mode in ["force", "append"]:
            audience_group_id = self.get_audience_gid_by_name(audience_group_name)
            if audience_group_id is not None and mode == "force":
                self.delete_audience_group(audience_group_id)
            elif audience_group_id is not None and mode == "append":
                self.add_audiences_to_audience_group(audience_group_id, audiences)
                return audience_group_id
        return super(LineBotApi, self).create_audience_group(
            audience_group_name, audiences, is_ifa, timeout)

    def get_audience_gid_by_name(self, description, timeout=None):
        audience_groups = super(LineBotApi, self).get_audience_group_list(
            description=description, timeout=timeout)
        for audience_group in audience_groups:
            if audience_group.description == description:
                return audience_group.audience_group_id
        else:
            return None

    def delete_audience_groups(self, audienceGroupIds):
        for audienceGroupId in audienceGroupIds:
            if audienceGroupId is not None:
                self.delete_audience_group(audienceGroupId)


def initialize_env():
    _audience_group_id = [line_bot_api.get_audience_gid_by_name(gn) for gn in line_ids.keys()]
    _audience_group_id += [line_bot_api.get_audience_gid_by_name(gn + "_new")
                           for gn in line_ids.keys()]
    _audience_group_id += [line_bot_api.get_audience_gid_by_name(gn) for gn in
                           ['test_impression_based', 'test_click_based']]
    line_bot_api.delete_audience_groups(_audience_group_id)


def add_audience_groups_cust(mode="normal"):
    _audience_group_ids = []
    for audience_name, line_id in line_ids.items():
        if len(line_id) > 0:
            audience_ids = [{"Id": _id} for _id in line_id]
            new_gid = line_bot_api.create_audience_group(audience_name, audience_ids, mode=mode)
            _audience_group_ids.append(new_gid)
    return _audience_group_ids


def main():
    initialize_env()
    to_be_delete = []

    # Test create_imp_audience_group
    _audience_group_id = line_bot_api.create_imp_audience_group(
        'test_impression_based', request_id)
    to_be_delete.append(_audience_group_id)
    logging.info("create_imp_audience_group result :\n{}".format(_audience_group_id))

    # Test create_click_audience_group
    _audience_group_id = line_bot_api.create_click_audience_group('test_click_based', request_id)
    to_be_delete.append(_audience_group_id)
    logging.info("create_click_audience_group result :\n{}".format(_audience_group_id))

    # Test create_audience_group (normal)
    _audience_group_ids = add_audience_groups_cust()
    logging.info("create_audience_group(normal) result :\n{}".format(_audience_group_ids))

    # Test create_audience_group (force)
    _audience_group_ids = add_audience_groups_cust("force")
    logging.info("create_audience_group(force) result :\n{}".format(_audience_group_ids))

    # Test create_audience_group (append)
    _audience_group_ids = add_audience_groups_cust("append")
    logging.info("create_audience_group(append) result :\n{}".format(_audience_group_ids))

    # Test get_audience_group_list
    _audience_group_ids = [line_bot_api.get_audience_gid_by_name(gn) for gn in line_ids.keys()]
    logging.info("get_audience_group_list result :\n{}".format(_audience_group_ids))

    # Test rename_audience_group
    [line_bot_api.rename_audience_group(gid, gn + "_new")
     for gn, gid in zip(line_ids.keys(), _audience_group_ids)]

    # Test add_audiences_to_audience_group
    [line_bot_api.add_audiences_to_audience_group(gid, [{"Id": _id} for _id in tester[-3:]],
                                                  upload_description='test_{}'.format(gid))
     for gid in _audience_group_ids]

    # Test list all audience groups
    _audience_groups = line_bot_api.get_audience_group(_audience_group_ids[1])
    logging.info("Get audience group by 1st id  :\n{}".format(_audience_groups))

    # Test get_audience_group
    _audience_groups = [line_bot_api.get_audience_group(gid) for gid in _audience_group_ids]
    logging.info("get_audience_group result :\n{}".format(_audience_groups))

    # Test delete_audience_group
    [line_bot_api.delete_audience_group(gid) for gid in _audience_group_ids]

    # Test delete_audience_groups
    line_bot_api.delete_audience_groups(to_be_delete)

    # Test change_audience_group_authority_level
    line_bot_api.change_audience_group_authority_level('PUBLIC')

    # Test get_audience_group_authority_level
    _result = line_bot_api.get_audience_group_authority_level()
    logging.info("change_audience_group_authority_level result :\n{}".format(_result))

    # Test list all audience groups
    _audience_groups = line_bot_api.get_audience_group_list()
    logging.info("All audience groups :\n{}".format(_audience_groups))


if __name__ == '__main__':
    line_bot_api = LineBotApi(channel_access_token)
    main()
