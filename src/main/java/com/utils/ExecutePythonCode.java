package com.utils;

import java.io.IOException;

public class ExecutePythonCode {

	public static void executePythonScript(String pythonExePath, String pythonScriptPath, String inputJsonPath,
			String responseJsonPath, String outputJsonPath)
			throws IOException, InterruptedException, org.json.simple.parser.ParseException, IOException {
		
		System.out.println("Execution Started");
		ProcessBuilder pb = new ProcessBuilder(pythonExePath, pythonScriptPath, inputJsonPath, responseJsonPath, outputJsonPath);
		pb.redirectErrorStream(true);
		Process p = pb.start();
		p.waitFor();
		
		System.out.println(pythonExePath +" "+ pythonScriptPath + " "+inputJsonPath +" "+ responseJsonPath+" "+outputJsonPath);
		
		System.out.println("Execution Ended");
	}
}
