#!/usr/bin/env node

const fs = require("fs");
const path = require("path");

async function main() {
    const args = process.argv.slice(2);
    if (args.length < 1) {
        console.error("Usage: node decompile_class.js <class_name_or_file> [output_file]");
        process.exit(1);
    }

    let classInput = args[0];
    const outputFile = args[1];

    // If it's a file path, extract the class name
    let className = classInput;
    if (className.endsWith(".class")) {
        className = path.basename(className, ".class");
    }

    // Load the CFR decompile function from our installed tool
    const cfrPath = path.resolve(__dirname, "../tools/node_modules/@run-slicer/cfr/cfr.js");
    if (!fs.existsSync(cfrPath)) {
        console.error(`Error: CFR decompiler module not found at ${cfrPath}. Run npm install first.`);
        process.exit(1);
    }

    const { decompile } = require(cfrPath);

    const jarExtractedDir = path.resolve(__dirname, "../extracted/jar");

    try {
        const result = await decompile(className, {
            source: async (name) => {
                // First try to load from the same directory as input if it was a direct file
                if (fs.existsSync(classInput) && name === className) {
                    return fs.readFileSync(classInput);
                }
                // Otherwise load from research/extracted/jar
                const classPath = path.join(jarExtractedDir, name + ".class");
                if (fs.existsSync(classPath)) {
                    return fs.readFileSync(classPath);
                }
                return null;
            }
        });

        if (outputFile) {
            fs.writeFileSync(outputFile, result);
            console.log(`Decompiled successfully. Output saved to ${outputFile}`);
        } else {
            console.log(result);
        }
        console.log("Forcing hard exit with SIGKILL...");
        process.kill(process.pid, 'SIGKILL');
    } catch (err) {
        console.error("Decompilation error:", err);
        process.exit(1);
    }
}

main();
