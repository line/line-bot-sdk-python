package line.bot.generator.pebble;

import io.pebbletemplates.pebble.PebbleEngine;
import io.pebbletemplates.pebble.loader.ClasspathLoader;
import org.openapitools.codegen.api.AbstractTemplatingEngineAdapter;
import org.openapitools.codegen.api.TemplatingExecutor;

import java.io.IOException;
import java.io.StringWriter;
import java.util.Map;

public class PebbleTemplateAdapter extends AbstractTemplatingEngineAdapter {
    private static final String[] EXTENSIONS = new String[]{"pebble"};

    private final PebbleEngine engine = new PebbleEngine.Builder()
            .cacheActive(false)
            .newLineTrimming(false)
            .loader(buildLoader())
            .autoEscaping(false)
            .build();

    private static ClasspathLoader buildLoader() {
        // OpenAPI Generator passes the template file relative to templateDir
        // (e.g. "model.pebble"), so the loader resolves it under our template dir.
        ClasspathLoader loader = new ClasspathLoader();
        loader.setPrefix("python-nextgen-custom-client/");
        loader.setSuffix("");
        return loader;
    }

    public PebbleTemplateAdapter() {
        super();
    }

    @Override
    public String getIdentifier() {
        return "pebble";
    }

    @Override
    public String[] getFileExtensions() {
        return EXTENSIONS;
    }

    @Override
    public String compileTemplate(TemplatingExecutor generator, Map<String, Object> bundle, String templateFile) throws IOException {
        String modifiedTemplate = this.getModifiedFileLocation(templateFile)[0];

        StringWriter writer = new StringWriter();
        engine.getTemplate(modifiedTemplate).evaluate(writer, bundle);
        return writer.toString();
    }
}
