import { DOMAIN } from "../constants/api";
import { MatchData } from "@/types/matchTypes";

export async function fetchMatchData({
  server,
  summonerName,
}: {
  server: string;
  summonerName: string;
}): Promise<MatchData[]> {
  const response = await fetch(
    `${DOMAIN}/match_history/${server}/?summoner_name=${summonerName}`,
    { cache: "no-store" }
  );

  if (!response.ok) {
    const errorText = await response.text();
    console.error(`Error fetching match data: ${errorText}`);
    throw new Error(
      `Failed to fetch match data: ${response.status} ${response.statusText}`
    );
  }

  try {
    return await response.json();
  } catch (error: any) {
    console.error(`Error parsing JSON: ${error.message}`);
    throw new Error(`Invalid JSON response: ${error.message}`);
  }
}
