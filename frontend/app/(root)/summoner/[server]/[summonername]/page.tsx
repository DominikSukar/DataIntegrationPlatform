import Game from "@/components/game/Game";
import { MatchData, PageProps } from "@/types/matchTypes";
import { fetchMatchData } from "@/api/matchHistory";

const SummonerPage = async ({ params }: PageProps) => {
  const { server, summonerName } = params;
  const matches = await fetchMatchData(params);

  return (
    <div>
      <div>{summonerName} # {server}</div>
      <div className="flex flex-col items-center">
        {matches.map((match, index) => (
          <Game key={index} match={match} />
        ))}
      </div>
    </div>
  );
};

export default SummonerPage;
