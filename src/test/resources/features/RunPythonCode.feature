Feature: Compare JSON files

  Scenario Outline: Compare JSON files
    Given Inputs <pythonExePath> <pythonScriptPath> <inputJsonPath> <responseJsonPath> <outputJsonPath>
    When Compare Output JSON files <resultJsonPath> <outputJsonPath>

    Examples: 
      | pythonExePath | pythonScriptPath                        | inputJsonPath              | responseJsonPath               | resultJsonPath              | outputJsonPath              |
      | "python3"     | ".\\pythonfiles\\dcu_interpretation.py" | ".\\jsonfiles\\input.json" | "C.\\jsonfiles\\response.json" | ".\\jsonfiles\\result.json" | ".\\jsonfiles\\output.json" |
