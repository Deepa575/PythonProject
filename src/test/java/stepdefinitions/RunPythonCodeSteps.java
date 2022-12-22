package stepdefinitions;

import java.io.IOException;

import org.json.simple.parser.ParseException;

import com.utils.Compare2JsonFiles;
import com.utils.ExecutePythonCode;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

public class RunPythonCodeSteps {

	private ExecutePythonCode utils = new ExecutePythonCode();
	private Compare2JsonFiles cmp = new Compare2JsonFiles();

	@Given("Inputs {string} {string} {string} {string} {string}")
	public void inputs(String pythonExePath, String pythonScriptPath, String inputJsonPath, String responseJsonPath, String outputJsonPath) {
		try {
			utils.executePythonScript(pythonExePath, pythonScriptPath, inputJsonPath, responseJsonPath, outputJsonPath);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	@When("Compare Output JSON files {string} {string}")
	public void compare_output_json_files(String resultJsonPath, String outputJsonPath) throws IOException, ParseException {
		cmp.compare2JsonFiles(resultJsonPath, outputJsonPath);
	}
}
