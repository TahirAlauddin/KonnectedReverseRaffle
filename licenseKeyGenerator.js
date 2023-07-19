async function sendPostRequest(customer_name, contact_email) {
    // URL and payload
    const url = "https://svkml47yk3.execute-api.us-east-1.amazonaws.com/default/KonnectedReverseRaffleLambdaFunction";
    const data = {
      customer_name,
      contact_email
    };
    
    try {
      // Make a POST request
      const response = await fetch(url, {
        method: "POST",
        mode: "no-cors",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
      });
  
      // Handling the response
      if(response.ok) {
        const jsonResponse = await response.json();
        console.log("Response Data:", jsonResponse);
        return jsonResponse;
      } else {
        console.error("Error:", response.status, response.statusText);
      }
    } catch(error) {
      console.error("Network Error:", error);
    }
  }
  
  // Usage 
  sendPostRequest("John Doe", "john.doe@example.com");