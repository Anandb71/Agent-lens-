// Define the type HERE
export type Step = {
  id: number;
  step_type: string;
  content: string;
  session_id: number;
};

// This function runs on the server to load the data
export async function load({ params }) {
  const id = params.id; // Get the [id] from the URL
  const response = await fetch(`http://127.0.0.1:8000/session/${id}`);
  const steps: Step[] = await response.json();

  return {
    steps: steps // Pass the steps to the page
  };
}