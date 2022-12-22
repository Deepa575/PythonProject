package com.utils;

import java.io.FileReader;
import java.io.IOException;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import org.testng.Assert;
/**
 * This class is used to compare 2 JSON file Objects
 * @author Deepa
 *
 */
public class Compare2JsonFiles {
	/**
	 * This method is used to compare 2 JSON file Objects using JSON file path
	 * @param resultJsonPath
	 * @param outputJsonPath
	 * @throws IOException
	 * @throws ParseException
	 */
	public void compare2JsonFiles(String resultJsonPath, String outputJsonPath) throws IOException, ParseException {

		// Creating a JSON parser object
		JSONParser jsonparser = new JSONParser();

		// Reading the JSON files
		FileReader result_read = new FileReader(resultJsonPath);
		FileReader output_read = new FileReader(outputJsonPath);

		//parsing the content of JSON files
		JSONArray resultJsonArray = (JSONArray) jsonparser.parse(result_read);
		JSONArray ouputJsonArray = (JSONArray) jsonparser.parse(output_read);

		//Retrieving JSON Object from JSON Array
		JSONObject Object11 = (JSONObject) resultJsonArray.get(0);
		JSONObject Object21 = (JSONObject) ouputJsonArray.get(0);
		
		//Retrieving JSON Array '0xF0' from JSON Object
		JSONArray array11 = (JSONArray) Object11.get("0xF0");
		JSONArray array21 = (JSONArray) Object21.get("0xF0");

		//Retrieving 1st Object from 0xF0 Array
		JSONObject resultObject = (JSONObject) array11.get(0);
		JSONObject ouputObject = (JSONObject) array21.get(0);

		//Retrieving 0x11 JSON Array from JSON Object
		JSONArray resultarr = (JSONArray) resultObject.get("0x11");
		JSONArray outputarr = (JSONArray) ouputObject.get("0x11");

		//Comparing JSON Object elements of 0x11 Array
		for (int k = 0; k < resultarr.size(); k++) {
			JSONObject resultArrayEleObj = (JSONObject) resultarr.get(k);
			JSONObject outputArrayEleObj = (JSONObject) outputarr.get(k);
			Assert.assertEquals(resultArrayEleObj.get("ErrorType"), outputArrayEleObj.get("ErrorType"));
			Assert.assertEquals(resultArrayEleObj.get("left_door_cumulative_count"),
					outputArrayEleObj.get("left_door_cumulative_count"));
			
			Assert.assertEquals(resultArrayEleObj.get("left_door_occurrence_count"),
					outputArrayEleObj.get("left_door_occurrence_count"));
			
			Assert.assertEquals(resultArrayEleObj.get("right_door_cumulative_count"),
					outputArrayEleObj.get("right_door_cumulative_count"));
			
			Assert.assertEquals(resultArrayEleObj.get("right_door_occurrence_count"),
					outputArrayEleObj.get("right_door_occurrence_count"));			
		}
		System.out.println("0xF0 - 0x11 JSON Array Verified ");
		
		//0xF0 - 0x03 Comparison
		JSONObject resultObject_0x03 = (JSONObject) array11.get(1);
		JSONObject ouputObject_0x03 = (JSONObject) array21.get(1);
		
		JSONArray resultarr_0x03 = (JSONArray) resultObject_0x03.get("0x03");
		JSONArray outputarr_0x03 = (JSONArray) ouputObject_0x03.get("0x03");
		
		JSONObject resultArrayEleObj_0x03 = (JSONObject) resultarr_0x03.get(0);
		JSONObject outputArrayEleObj_0x03 = (JSONObject) outputarr_0x03.get(0);
		Assert.assertEquals(resultArrayEleObj_0x03.get("door_type"), outputArrayEleObj_0x03.get("door_type"));
		Assert.assertEquals(resultArrayEleObj_0x03.get("motor1_sys_cyc_count"), outputArrayEleObj_0x03.get("motor1_sys_cyc_count"));
		Assert.assertEquals(resultArrayEleObj_0x03.get("motor2_sys_cyc_count"), outputArrayEleObj_0x03.get("motor2_sys_cyc_count"));
		System.out.println("0xF0 - 0x03 JSON Array Verified ");
		
		//0xF0 - 0x00 Comparison
		JSONObject resultObject_0x00 = (JSONObject) array11.get(2);
		JSONObject ouputObject_0x00 = (JSONObject) array21.get(2);
		
		JSONArray resultarr_0x00 = (JSONArray) resultObject_0x00.get("0x00");
		JSONArray outputarr_0x00 = (JSONArray) ouputObject_0x00.get("0x00");
		
		JSONObject resultArrayEleObj_0x00 = (JSONObject) resultarr_0x00.get(0);
		JSONObject outputArrayEleObj_0x00 = (JSONObject) outputarr_0x00.get(0);
		
		Assert.assertEquals(resultArrayEleObj_0x00.get("status_value"), outputArrayEleObj_0x00.get("status_value"));
		Assert.assertEquals(resultArrayEleObj_0x00.get("lcp_firm_version"), outputArrayEleObj_0x00.get("lcp_firm_version"));
		System.out.println("0xF0 - 0x00 JSON Array Verified ");
		
		//0xF0 - 0x10 Comparison
		JSONObject resultObject_0x10 = (JSONObject) array11.get(3);
		JSONObject ouputObject_0x10 = (JSONObject) array21.get(3);
		
		JSONArray resultarr_0x10 = (JSONArray) resultObject_0x10.get("0x10");
		JSONArray outputarr_0x10 = (JSONArray) ouputObject_0x10.get("0x10");
		
		JSONObject resultArrayEleObj_0x10 = (JSONObject) resultarr_0x10.get(0);
		JSONObject outputArrayEleObj_0x10 = (JSONObject) outputarr_0x10.get(0);
		
		Assert.assertEquals(resultArrayEleObj_0x10.get("status_value"), outputArrayEleObj_0x10.get("status_value"));
		Assert.assertEquals(resultArrayEleObj_0x10.get("mcp_firm_version"), outputArrayEleObj_0x10.get("mcp_firm_version"));
		System.out.println("0xF0 - 0x10 JSON Array Verified ");
		
		//0xF0 - 0x1E Comparison
		JSONObject resultObject_0x1E = (JSONObject) array11.get(4);
		JSONObject ouputObject_0x1E = (JSONObject) array21.get(4);
		
		JSONArray resultarr_0x1E = (JSONArray) resultObject_0x1E.get("0x1E");
		JSONArray outputarr_0x1E = (JSONArray) ouputObject_0x1E.get("0x1E");
		
		JSONObject resultArrayEleObj_0x1E = (JSONObject) resultarr_0x1E.get(0);
		JSONObject outputArrayEleObj_0x1E = (JSONObject) outputarr_0x1E.get(0);
		
		Assert.assertEquals(resultArrayEleObj_0x1E.get("switch_mode_value"), outputArrayEleObj_0x1E.get("switch_mode_value"));
		System.out.println("0xF0 - 0x1E JSON Array Verified ");
		
		//0xF0 - 0x01 Comparison
		JSONObject resultObject_0x01 = (JSONObject) array11.get(5);
		JSONObject ouputObject_0x01 = (JSONObject) array21.get(5);
		
		JSONArray resultarr_0x01 = (JSONArray) resultObject_0x01.get("0x01");
		JSONArray outputarr_0x01 = (JSONArray) ouputObject_0x01.get("0x01");
		
		JSONObject resultArrayEleObj_0x01 = (JSONObject) resultarr_0x01.get(0);
		JSONObject outputArrayEleObj_0x01 = (JSONObject) outputarr_0x01.get(0);
		Assert.assertEquals(resultArrayEleObj_0x01.get("system_cycle_count"), outputArrayEleObj_0x01.get("system_cycle_count"));
		Assert.assertEquals(resultArrayEleObj_0x01.get("active_door_id"), outputArrayEleObj_0x01.get("active_door_id"));
		Assert.assertEquals(resultArrayEleObj_0x01.get("original_door_id"), outputArrayEleObj_0x01.get("original_door_id"));
		System.out.println("0xF0 - 0x01 JSON Array Verified ");
		
		//0xF1
		JSONObject Object12 = (JSONObject) resultJsonArray.get(1);
		JSONObject Object22 = (JSONObject) resultJsonArray.get(1);
		JSONArray array12 = (JSONArray) Object12.get("0xF1");
		JSONArray array22 = (JSONArray) Object22.get("0xF1");
		
		//0xF1 - 0x11 Comparison
		JSONObject resultObject2 = (JSONObject) array12.get(0);
		JSONObject ouputObject2 = (JSONObject) array22.get(0);

		JSONArray resultarr2 = (JSONArray) resultObject2.get("0x11");
		JSONArray outputarr2 = (JSONArray) ouputObject2.get("0x11");

		for (int k = 0; k < resultarr2.size(); k++) {
			JSONObject resultArrayEleObj2 = (JSONObject) resultarr2.get(k);
			JSONObject outputArrayEleObj2 = (JSONObject) outputarr2.get(k);
			Assert.assertEquals(resultArrayEleObj2.get("ErrorType"), outputArrayEleObj2.get("ErrorType"));
			Assert.assertEquals(resultArrayEleObj2.get("left_door_cumulative_count"),
					outputArrayEleObj2.get("left_door_cumulative_count"));
			
			Assert.assertEquals(resultArrayEleObj2.get("left_door_occurrence_count"),
					outputArrayEleObj2.get("left_door_occurrence_count"));
			
			Assert.assertEquals(resultArrayEleObj2.get("right_door_cumulative_count"),
					outputArrayEleObj2.get("right_door_cumulative_count"));
			
			Assert.assertEquals(resultArrayEleObj2.get("right_door_occurrence_count"),
					outputArrayEleObj2.get("right_door_occurrence_count"));			
		}
		System.out.println("0xF1 - 0x11 JSON Array Verified ");
		
		System.out.println("Comparison Completed & 2 JSON files are Matching Exactly");	
	}
}
