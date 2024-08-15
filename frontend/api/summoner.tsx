import { DOMAIN } from "../constants/api";
import { SummonerData } from "@/types/matchTypes";

export async function fetchSummonerData({
  server,
  summonerName,
}: {
  server: string;
  summonerName: string;
}): Promise<SummonerData> {
  const response = await fetch(
    `${DOMAIN}/summoner/${server}/?summoner_name=${summonerName}`,
    { next: { revalidate: 3600 } }
  );

  if (!response.ok) {
    const errorText = await response.text();
    console.error(`Error fetching summoner data: ${errorText}`);
    throw new Error(
      `Failed to fetch summoner data: ${response.status} ${response.statusText}`
    );
  }

  try {
    return await response.json();
  } catch (error: any) {
    console.error(`Error parsing JSON: ${error.message}`);
    throw new Error(`Invalid JSON response: ${error.message}`);
  }
}
