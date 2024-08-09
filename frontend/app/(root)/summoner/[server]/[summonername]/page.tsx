import Game from "@/components/Game";
import { MatchData, PageProps } from "@/types/matchTypes";

async function fetchMatchData(server: string, summonerName: string): Promise<MatchData[]> {
  const response = await fetch(`http://localhost:8000/match_history/${server}/?summoner_name=${summonerName}`, {cache: 'no-store'});

  return response.json();
}

const SummonerPage = async ({ params }: PageProps) => {
  const { server, summonername } = params;
  const matches = await fetchMatchData(server, summonername);

  return (
    <div>
      <div>{summonername} # {server}</div>
      <div className="flex flex-col items-center">
        {matches.map((match, index) => (
          <Game key={index} match={match} />
        ))}
      </div>
    </div>
  );
};

export default SummonerPage;
