import java.io.*;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;


/**
 * Class for getting names of prescription drugs from NDC (National Drug Code) database.
 */
public class NameGetter {
    private static final String INPUT_FILE = "data/product.txt";

    /**
     * Saves names to output file.
     * <p>
     * Collects only single-word names of human prescription drugs that
     * do not contain hyphens or slashes. Converts names to lowercase.
     * Writes names into output file.
     *
     * @param output file into which names are to be written.
     */
    public static void namesToFile(File output) {
        try (FileWriter writer = new FileWriter(output)) {
            Files.readAllLines(Paths.get(INPUT_FILE), Charset.forName("ISO-8859-1"))
                    .stream()
                    .map(s -> s.split("\t"))
                    .filter(s -> "HUMAN PRESCRIPTION DRUG".equals(s[2]))
                    .map(s -> s[3])
                    .filter(s -> s.split(" ").length == 1)
                    .filter(s -> !s.contains("/"))
                    .filter(s -> !s.contains("-"))
                    .distinct()
                    .map(String::toLowerCase)
                    .map(s -> s + "\n")
                    .forEach(s -> {
                        try {
                            writer.write(s);
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                    });


        } catch (Exception e) {
            e.printStackTrace();
        }

    }

    public static void main(String[] args) {
        NameGetter.namesToFile(new File("names.txt"));
    }


}
