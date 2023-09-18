import requests
import json
import os

base_url = "https://ob.gocardless.com"
newT_url = "/api/v2/token/new/"
refT_url = "/api/v2/token/refresh/"
#Mandatory to enter secret_id variable.
secret_id = (input("Enter your secret_id: "))
#for testing purposes we can define variable..
#secret_id = "" #for testing purposes.
#Mandatory to enter secret_id variable.
secret_key = (input("Enter your secret_key: "))
#for testing purposes we can define variable..
#secret_key = ""
empty_json={
  "access": "string",
  "access_expires": 0,
  "refresh": "string",
  "refresh_expires": 0,
  "secret_id":"string"
}
          
def new_token():
         # Firstly we check fiel, if it is empty we do not check token, or token expertion. Than we will create new token.
         f = open("user_data.json","w") # creating file to store user data.
         check_file = os.path.getsize("user_data.json")
         if(check_file == 0):
            print("No user data - requesting NEW token.")
            #Here we saving in file json. structure to run checks.
            tjson_str = json.dumps(empty_json, indent=4)
            with open("user_data.json", "w") as outfile:
               outfile.write(tjson_str)
         else:
            print("Cheking for existing token.")

         with open("user_data.json", "r") as openfile:
               json_object= json.load(openfile)
               # we check if there is not expired token in file and returning token if it exists.
               if json_object["secret_id"] == secret_id and json_object["access_expires"] > 0 :
                   print("You alredy have TOKEN : ",(json_object["access"]))
                   quit()
               # we check if there is expired token in file.
               elif json_object["secret_id"] == secret_id and json_object["access_expires"] == 0:
                   print(json_object["secret_id"] != secret_id and json_object["access_expires"] == 0)
                   print("Token is expired. Refreshing token.")
                   refresh = json_object["refresh"]
                   refresh_token(refresh)     
                   quit()   
               # if no token found, we genereting new token.                   
               else:
                   print("No token found. Genereting new token.")
         # call to generate new token.
         url = base_url + newT_url #"https://ob.gocardless.com/api/v2/token/new/"
         print("post url:"+ url)
         data = {
           "secret_id": secret_id,
           "secret_key": secret_key
         }
         response = requests.post(url, json=data)
         assert response.status_code == 200 #checking response code.
         json_data = response.json()
         json_data["secret_id"]=secret_id # adding user secret to file, to be possible to found that user have received token.
         json_str = json.dumps(json_data, indent=4)
         #print("json new token response body:",json_str)
         access = json_data["access"]
         refresh = json_data["refresh"]
         access_expires = json_data["access_expires"]
         refresh_expires = json_data["refresh_expires"]
         #saving new generated token data to file.
         with open("user_data.json", "w") as outfile:
              outfile.write(json_str)

         print("Your new token is:",access)
         print("Your new token access expires in :",access_expires)
         print("Your new refresh token is:",refresh)
         print("Your new refresh token access expires in :",refresh_expires)
        
# refreshing token.
def refresh_token(refresh):
    #call to refresh token.
    url = base_url + refT_url #"https://ob.gocardless.com/api/v2/token/refresh/"
    print("post url:"+ url)
    data={
       "refresh": refresh
    }
    
    response = requests.post(url, json=data)
    assert response.status_code == 200
    json_data = response.json()
    json_data["secret_id"]=secret_id # adding user secret to file, to be possible to found that user have refreshed token.
    json_str = json.dumps(json_data, indent=4)
    #print("json refresh token response body:",json_str)
    access = json_data["access"]
    access_expires = json_data["access_expires"]
    print("Your refreshed token is:",access)
    print("Your refreshed token access expires in :",access_expires)
    #saving refreshed token data to file.
    with open("user_data.json", "w") as outfile:
              outfile.write(json_str)
    return access 
    
new_token()


