package runPythonCode;

import java.io.FileReader;
import java.io.IOException;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class ReadDataFromJSONFile {

	public static void main(String[] args) throws IOException, ParseException {
		
		//Creating a JSON parser object
		JSONParser jsonparser = new JSONParser();
		
		//parsing the content of JSON file
		FileReader reader = new FileReader(".\\jsonfiles\\input.json");
		
		Object obj = jsonparser.parse(reader);
		
		JSONObject inputJsonObj = (JSONObject) obj;
		//JSONObject inputJsonObj = (JSONObject) jsonparser.parse(new FileReader(".\\jsonfiles\\input.json"));
		
		//Reading the data from the json file
		JSONObject metadata = (JSONObject) inputJsonObj.get("Metadata");
		String configVerNo = (String) metadata.get("ConfigVerNo");
		System.out.println("ConfigVerNo: "+configVerNo);
		
		JSONObject doorType = (JSONObject) metadata.get("DoorType");
		String type = (String) doorType.get("Type");
		System.out.println("DoorType Type: "+ type);
		
		JSONObject firmwareVersionRange = (JSONObject) metadata.get("FirmwareVersionRange");
		String lowVersion = (String) firmwareVersionRange.get("LowVersion");
		System.out.println("FirmwareVersionRange LowVersion: "+lowVersion);
		
		String highVersion = (String) firmwareVersionRange.get("HighVersion");
		System.out.println("FirmwareVersionRange HighVersion: "+highVersion);
		
		JSONObject endpointCIUCloud = (JSONObject) metadata.get("endpoint_ciu_cloud");
		String awsHostname = (String) endpointCIUCloud.get("AWS_HOSTNAME");
		System.out.println("endpoint_ciu_cloud AWS_HOSTNAME: "+awsHostname);
		
		String deviceProfileId = (String) metadata.get("Device_profile_id");
		System.out.println("Device_profile_id: "+deviceProfileId);
		
		// get DataCommandGroup array from the JSON Object and store it into JSONArray  
		JSONArray dataCmdGrpArray = (JSONArray) inputJsonObj.get("DataCommandGroup");
		  
        for (int i = 0; i < dataCmdGrpArray.size(); i++) {  
            JSONObject explrObject = (JSONObject) dataCmdGrpArray.get(i);
            System.out.println("-------------------------");
            System.out.println("DataCommandGroup Array "+i+":");
            System.out.println("-------------------------");
            
            String id = (String) explrObject.get("ID");
            System.out.println("DataCommandGroup ID: "+id);
            
            String name = (String) explrObject.get("Name");
            System.out.println("DataCommandGroup Name: "+name);
            
            String pollTime = (String) explrObject.get("PollTime");
            System.out.println("DataCommandGroup PollTime: "+pollTime);
            
            String transmitTime = (String) explrObject.get("TransmitTime");
            System.out.println("DataCommandGroup TransmitTime: "+transmitTime);
            
            String active = (String) explrObject.get("Active");
            System.out.println("DataCommandGroup Active: "+active);
            
//            String priority = (String) explrObject.get("Priority");
//            System.out.println("DataCommandGroup Priority: "+priority);
            
            String transmitOnChange = (String) explrObject.get("TransmitOnChange");
            System.out.println("DataCommandGroup TransmitOnChange: "+transmitOnChange);
            
            JSONArray listArray = (JSONArray) explrObject.get("List");
            for (int j = 0; j < listArray.size(); j++) {
            	String list = (String) listArray.get(j);
            	System.out.println("DataCommandGroup List: "+list);
            }
            
            JSONArray commandsArray = (JSONArray) explrObject.get("Commands");
            for (int k = 0; k < commandsArray.size(); k++) {
            	JSONObject Object = (JSONObject) commandsArray.get(i);
            	System.out.println("DataCommandGroup Commands Array "+k+":");
                System.out.println("-----------------------------------");
            	
            	String ID = (String) Object.get("ID");
            	System.out.println("DataCommandGroup Commands ID: "+ID);
            	
            	String Active = (String) Object.get("Active");
            	System.out.println("DataCommandGroup Commands Active: "+Active);
            	
            	JSONArray cmdArray = (JSONArray) Object.get("Cmd");
            	for(int a=0;a<cmdArray.size();a++) {
            		String cmdArrayValue = (String) cmdArray.get(a);
            		System.out.println("DataCommandGroup Commands Cmd: "+cmdArrayValue);
            	}
            	
            }
            
        }}
	
}
