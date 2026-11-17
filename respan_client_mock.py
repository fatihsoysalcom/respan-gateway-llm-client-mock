import json
import os

# In a real scenario, you would use a library like 'requests' for HTTP calls.
# For this self-contained example, we'll simulate the HTTP interaction.

# --- Configuration ---
# The hypothetical URL for your Respan Gateway instance.
# In a real application, this would be a running server.
RESPAN_GATEWAY_URL = os.getenv("RESPAN_GATEWAY_URL", "http://localhost:8000/v1/chat/completions")
# You might also have an API key for the gateway itself
RESPAN_API_KEY = os.getenv("RESPAN_API_KEY", "sk-respan-mock-key")

def send_request_to_respan_gateway(prompt: str, model: str, temperature: float = 0.7):
    """
    Simulates sending a request to the Respan Gateway.
    This function demonstrates how a client application abstracts away the specific LLM provider
    (e.g., OpenAI, Anthropic) by routing all requests through the gateway.
    """
    print(f"--- Simulating Request to Respan Gateway ---")
    print(f"Gateway Endpoint: {RESPAN_GATEWAY_URL}")

    # The payload structure might vary, but typically includes model, messages, and parameters.
    # The Respan Gateway would then translate this into the specific provider's API call.
    payload = {
        "model": model, # The gateway might map this to a specific provider's model
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": temperature,
        # The gateway could also accept a 'provider' field to explicitly route,
        # or it could intelligently select one based on 'model' or other policies.
        # "provider": "openai" # Example of an optional gateway-specific field
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {RESPAN_API_KEY}" # Authenticate with the gateway
    }

    print("\nRequest Headers:")
    print(json.dumps(headers, indent=2))
    print("\nRequest Body (Payload):")
    print(json.dumps(payload, indent=2, ensure_ascii=False))

    # --- Simulate Gateway Response ---
    # In a real application, an HTTP POST request would be made here,
    # and the response would be parsed. For this example, we'll return a mocked response.
    print("\n--- Simulating Response from Respan Gateway ---")
    mock_response_data = {
        "id": "chatcmpl-mock-respan-12345",
        "object": "chat.completion",
        "created": 1701234567,
        "model": model,
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": f"Merhaba! Respan Gateway üzerinden '{prompt}' isteğiniz başarıyla işlendi. Bu, {model} modelinin simüle edilmiş bir yanıtıdır."
                },
                "logprobs": None,
                "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": len(prompt.split()), # Simple token count mock
            "completion_tokens": 25,
            "total_tokens": len(prompt.split()) + 25
        },
        "gateway_info": { # Gateway-specific information could be added here for cost/performance insights
            "routed_provider": "mock_openai",
            "cost_estimation_usd": 0.0015,
            "latency_ms": 150
        }
    }

    print("Response Status: 200 OK")
    print("Response Body:")
    print(json.dumps(mock_response_data, indent=2, ensure_ascii=False))

    return mock_response_data

if __name__ == "__main__":
    # Example usage:
    user_prompt = "Büyük Dil Modelleri (LLM) nedir ve neden önemlidir?"
    desired_model = "gpt-4-turbo" # The gateway would map this to an actual provider's model

    print("--- Client Application Starting ---")
    # This highlights the core concept: client interacts with the gateway, not directly with LLMs.
    print("The client interacts with Respan Gateway, abstracting away direct LLM provider details.")

    # Send the request through the simulated gateway
    response = send_request_to_respan_gateway(user_prompt, desired_model)

    print("\n--- Client Application Received Response ---")
    if response and "choices" in response and response["choices"]:
        assistant_message = response["choices"][0]["message"]["content"]
        print(f"Assistant's Reply: {assistant_message}")
        if "gateway_info" in response:
            print(f"Gateway Info: Routed via {response['gateway_info']['routed_provider']}, Estimated Cost: ${response['gateway_info']['cost_estimation_usd']}")
    else:
        print("Failed to get a valid response from the gateway.")

    print("\n--- End of Example ---")
    print("This demonstrates how Respan Gateway simplifies LLM interaction by providing a unified API.")
