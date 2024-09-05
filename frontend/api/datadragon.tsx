import { DOMAIN } from "../constants/api";


export async function fetchSummoners(): Promise<any> {
  const response = await fetch(`${DOMAIN}/datadragon/summoners/`, {
    next: { revalidate: 3600 },
  });

  if (!response.ok) {
    const errorText = await response.text();
    console.error(`Error fetching item data: ${errorText}`);
    throw new Error(
      `Failed to fetch item data: ${response.status} ${response.statusText}`
    );
  }

  try {
    return await response.json();
  } catch (error: any) {
    console.error(`Error parsing JSON: ${error.message}`);
    throw new Error(`Invalid JSON response: ${error.message}`);
  }
}

export async function fetchPerks(): Promise<any> {
  const response = await fetch(`${DOMAIN}/datadragon/perks/`, {
    next: { revalidate: 3600 },
  });

  if (!response.ok) {
    const errorText = await response.text();
    console.error(`Error fetching item data: ${errorText}`);
    throw new Error(
      `Failed to fetch item data: ${response.status} ${response.statusText}`
    );
  }

  try {
    return await response.json();
  } catch (error: any) {
    console.error(`Error parsing JSON: ${error.message}`);
    throw new Error(`Invalid JSON response: ${error.message}`);
  }
}
