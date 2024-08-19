import { DOMAIN } from "../constants/api";
import { MatchData } from "@/types/matchTypes";

export async function fetchItems(): Promise<any> {
  const response = await fetch(`${DOMAIN}/datadragon/items/`, {
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
