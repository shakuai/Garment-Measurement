# Shaku - Garment Measurement API
An AI-powered solution that automatically measures garments from images using computer vision and deep learning. Upload your T-shirt images following simple guidelines, and the API accurately calculates key dimensions such as length, chest width, and waist width,  enabling precise digital garment measurement for e-commerce, manufacturing, and virtual fitting applications.

---
<img width="1181" height="1181" alt="garment_measurement" src="https://github.com/user-attachments/assets/b3e8b083-1bfd-49c2-b452-008c65f9faa6" />



## Overview

The Garment Measurement API by Shaku provides an intelligent solution for extracting precise measurements from garment images using advanced computer vision and deep learning models. This API is designed for fashion retailers, manufacturers, and e-commerce platforms that need to accurately measure clothing dimensions from flat-lay images, without manual tools or human intervention.

By simply uploading an image of a garment (currently optimized for T-shirts), the API calculates key metrics.
It also validates image quality to ensure compliance with measurement guidelines and guarantees consistent accuracy across different lighting and background conditions.

## Image Capture Guidelines
To achieve the most accurate results, make sure to follow these instructions when uploading your garment images:

  1. Ensure the garment is a T-shirt (other garment types coming soon).

  2. Capture the entire front view of the T-shirt in portrait orientation — avoid tilted or rotated images.

  3. Place a flat A4 sheet next to the T-shirt for scale (do not place it on top), ensuring it has no folds or wrinkles.

  4. All corners of both the T-shirt and the A4 sheet must be fully visible in the image.

  5. Use a flat surface with a plain, uncluttered background.

  6. Avoid shadows or reflections for accurate measurements.

  7. Keep each image under 3MB.

  8. You can upload up to 50 images in one batch.

These conditions allow the AI model to establish an accurate reference scale and calculate real-world dimensions precisely.

## How It Works

The Garment Measurement API uses a hybrid pipeline combining image segmentation, edge detection, and geometric scaling based on the reference A4 sheet.
The model automatically:

  - Detects garment boundaries.

  - Identifies measurement points.

  - Converts pixel distances into centimeters using the A4 sheet as a known dimension.

  - Returns structured data with detailed metrics and positional metadata.

This automation significantly reduces manual effort in product digitization pipelines, ensuring consistency and precision for online catalogs or virtual fitting applications.

## Integration

### 1. API Integration

Developers can integrate the Garment Measurement API directly into websites, product management systems, or mobile applications.
The API provides a RESTful interface for uploading garment images and receiving structured JSON responses containing measurement data.

You can test and monitor your API usage through the Shaku Dashboard:
[Shaku Dashboard - Login & Test](https://dashboard.shaku.tech/auth/login)

Below are example HTTP requests for Python, PHP, and Node.js that can also be executed in Postman.

#### 1.1. Authentication (API Tokens)
 - **Get Access Token**
   
   Use this endpoint to log in with client ID, client secret, username, and password to receive an access token.
   
   - **Python**
      ```python
      import requests
      import json
      
      url = "https://api.shaku.tech/oauth/token"
      
      payload = json.dumps({
        "grant_type": "password",
        "client_id": "YOUR_CLIENT_ID",
        "client_secret": "YOUR_SECRET_KEY",
        "username": "YOUR_EMAIL_ADDRESS",
        "password": "YOUR_PASSWORD"
      })
      headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      }
      
      response = requests.request("POST", url, headers=headers, data=payload)
      
      print(response.text)
      
      ```

   - **PHP**
      ```php
      <?php
      
      $curl = curl_init();
      
      curl_setopt_array($curl, array(
        CURLOPT_URL => 'https://api.shaku.tech/oauth/token',
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_ENCODING => '',
        CURLOPT_MAXREDIRS => 10,
        CURLOPT_TIMEOUT => 0,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
        CURLOPT_CUSTOMREQUEST => 'POST',
        CURLOPT_POSTFIELDS =>'{
          "grant_type":"password",
          "client_id":"YOUR_CLIENT_ID",
          "client_secret":"YOUR_SECRET_KEY",
          "username":"YOUR_EMAIL_ADDRESS",
          "password":"YOUR_PASSWORD"
      }',
        CURLOPT_HTTPHEADER => array(
          'Content-Type: application/json',
          'Accept: application/json'
        ),
      ));
      
      $response = curl_exec($curl);
      
      curl_close($curl);
      echo $response;

      ```
   - **Node.Js**
      ```javascript
      var request = require('request');
      var options = {
        'method': 'POST',
        'url': 'https://api.shaku.tech/oauth/token',
        'headers': {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify({
          "grant_type": "password",
          "client_id": "YOUR_CLIENT_ID",
          "client_secret": "YOUR_SECRET_KEY",
          "username": "YOUR_EMAIL_ADDRESS",
          "password": "YOUR_PASSWORD"
        })
      
      };
      request(options, function (error, response) {
        if (error) throw new Error(error);
        console.log(response.body);
      });

      ```
  - **Refresh Token**
    
    Refresh the access token when it expires.
     
    - **Python**
      ```python
      import requests
      import json
      
      url = "https://api.shaku.tech/oauth/token"
      
      payload = json.dumps({
        "grant_type": "refresh_token",
        "refresh_token": "YOUR_REFRESH_TOKEN",
        "client_id": "YOUR_CLIENT_ID",
        "client_secret": "YOUR_SECRET_KEY"
      })
      headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      }
      
      response = requests.request("POST", url, headers=headers, data=payload)
      
      print(response.text)
      
      ```

    - **PHP**
      ```php
      <?php
      
      $curl = curl_init();
      
      curl_setopt_array($curl, array(
        CURLOPT_URL => 'https://api.shaku.tech/oauth/token',
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_ENCODING => '',
        CURLOPT_MAXREDIRS => 10,
        CURLOPT_TIMEOUT => 0,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
        CURLOPT_CUSTOMREQUEST => 'POST',
        CURLOPT_POSTFIELDS =>'{
          "grant_type":"refresh_token",
          "refresh_token":"YOUR_REFRESH_TOKEN",
          "client_id":"YOUR_CLIENT_ID",
          "client_secret":"YOUR_SECRET_KEY"
      }',
        CURLOPT_HTTPHEADER => array(
          'Content-Type: application/json',
          'Accept: application/json'
        ),
      ));
      
      $response = curl_exec($curl);
      
      curl_close($curl);
      echo $response;


      ```
    - **Node.Js**
      ```javascript
      var request = require('request');
      var options = {
        'method': 'POST',
        'url': 'https://api.shaku.tech/oauth/token',
        'headers': {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify({
          "grant_type": "refresh_token",
          "refresh_token": "YOUR_REFRESH_TOKEN",
          "client_id": "YOUR_CLIENT_ID",
          "client_secret": "YOUR_SECRET_KEY"
        })
      
      };
      request(options, function (error, response) {
        if (error) throw new Error(error);
        console.log(response.body);

      ```

   - **Revoke Token**
    
     Revoke an access token to log out or terminate access.
     
     - **Python**
       ```python
       import requests
       
       url = "https://api.shaku.tech/api/v1/auth/revoke"
       
       payload = ""
       headers = {
         'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
       }
       
       response = requests.request("GET", url, headers=headers, data=payload)
       
       print(response.text)
            
       ```

     - **PHP**
       ```php
       <?php
       
       $curl = curl_init();
       
       curl_setopt_array($curl, array(
         CURLOPT_URL => 'https://api.shaku.tech/api/v1/auth/revoke',
         CURLOPT_RETURNTRANSFER => true,
         CURLOPT_ENCODING => '',
         CURLOPT_MAXREDIRS => 10,
         CURLOPT_TIMEOUT => 0,
         CURLOPT_FOLLOWLOCATION => true,
         CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
         CURLOPT_CUSTOMREQUEST => 'GET',
         CURLOPT_HTTPHEADER => array(
           'Authorization: Bearer YOUR_ACCESS_TOKEN'
         ),
       ));
       
       $response = curl_exec($curl);
       
       curl_close($curl);
       echo $response;
 
 
       ```
     - **Node.Js**
       ```javascript
       var request = require('request');
       var options = {
         'method': 'GET',
         'url': 'https://api.shaku.tech/api/v1/auth/revoke',
         'headers': {
           'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
         }
       };
       request(options, function (error, response) {
         if (error) throw new Error(error);
         console.log(response.body);
       });
       ```

#### 1.2. Garment Measurement API Service

  This service accurately extracts detailed measurements from ،T-shirt images by using computer vision and AI-based scaling (via an A4 reference sheet).

  - **Python**
      ```python
      import requests
      import json
      
      url = "https://api.shaku.tech/api/v1/services/garmentMeasurement"
      
      payload = json.dumps({
        "Image": "IMAGE_BASE64_FORMAT"
      })
      headers = {
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
      }
      
      response = requests.request("POST", url, headers=headers, data=payload)
      
      print(response.text)
           
      ```
      
- **PHP**
     ```php
      <?php
      
      $curl = curl_init();
      
      curl_setopt_array($curl, array(
        CURLOPT_URL => 'https://api.shaku.tech/api/v1/services/garmentMeasurement',
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_ENCODING => '',
        CURLOPT_MAXREDIRS => 10,
        CURLOPT_TIMEOUT => 0,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
        CURLOPT_CUSTOMREQUEST => 'POST',
        CURLOPT_POSTFIELDS =>'{
          "Image":"IMAGE_BASE64_FORMAT"
      }',
        CURLOPT_HTTPHEADER => array(
          'Authorization: Bearer YOUR_ACCESS_TOKEN'
        ),
      ));
      
      $response = curl_exec($curl);
      
      curl_close($curl);
      echo $response;
      

     ```
- **Node.Js**
    ```javascript

        var request = require('request');
        var options = {
          'method': 'POST',
          'url': 'https://api.shaku.tech/api/v1/services/garmentMeasurement',
          'headers': {
            'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            "Image": "IMAGE_BASE64_FORMAT"
          })
        
        };
        request(options, function (error, response) {
          if (error) throw new Error(error);
          console.log(response.body);
        });

    ```
        
### 2. SDK Integration
  
  For simpler and faster integration, you can test directly on the Dashboard or use the Python package.
  - [Shaku Dashboard - Login & Test](https://dashboard.shaku.tech/auth/login)
  - Install via PyPI:
    ```python
    pip install shakuapi
    ```
    
    Python Example:

    ```python
      from shakuapi import ShakuClient
      
      client = ShakuClient(client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET")
      
      # login
      client.login(username="YOUR_USERNAME", password="YOUR_PASSWORD")
      
      # get size measurement
      result = client.garment_measurement("garment_image.jpg")
      
      print(result)
    ```


## Pricing

Shaku offers a cost-effective and scalable solution that provides maximum features for online fashion and apparel businesses. By reducing return rates and improving customer satisfaction, Shaku helps businesses increase revenue and optimize operations. Pricing plans are designed to accommodate small shops to large enterprises, ensuring that every business can benefit from AI-powered garment measurement technology. For detailed pricing, subscription plans, and enterprise solutions, visit [Shaku Pricing](https://shaku.tech/#pricing)

## Application

Shaku’s mobile application also supports garment measurement, allowing users to capture high-quality T-shirt images directly from their smartphones.
The app provides real-time feedback, verifying lighting, background, and framing, before uploading to ensure the best accuracy.


## Privacy & Data Handling

- Uploaded images are processed and deleted immediately after inference.
- No personal data is stored or shared.

## Resources

- Official website: [Shaku.tech](https://shaku.tech)
- Documentation: [[API Reference]](https://api.shaku.tech/docs.html)


## License

MIT License © 2025 ShakuAI



