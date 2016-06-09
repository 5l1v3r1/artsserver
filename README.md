# Augmented Reality Tagging System Server

RESTful server which handles post requests from the webclient and returns content to the android application.

## Endpoints

The webclient makes the post request specifying the contentType and contentData and is responded to with a unique id for accessing the content in our Mongo database. The Android application makes a get request using the unique id and is returned the contentType and contentData.
 
### Posting Content (POST Method)

  Endpoint:
  ```
  http://artsserver.herokuapp.com/content/setContent
  ```

  JSON Form:
  ```  
  {
    'contentType': <image or text>, 
    'contentData': <data in text or base64 encoding>,
  }
  ```

  Response:
  ```
  <unique id>
  ```

### Getting Content (GET Method)

  Endpoint:
  ```
  http://artsserver.herokuapp.com/content/getContent/<unique id>
  ```

  Response:
  ```                                     
  {
    'contentType': <image or text>, 
    'contentData': <data in text or base64 encoding>,
  }
  ```

