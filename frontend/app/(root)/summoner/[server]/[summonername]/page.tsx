import User from "./User";
import Game from "./Game";

import { MatchData, PageProps } from "@/types/matchTypes";
import { DOMAIN } from "@/constants/api";

const SummonerPage = async ({ params }: PageProps) => {
  const { server, summonerName } = params;

  const response = await fetch(
    `${DOMAIN}/match_history/${server}/?summoner_name=${summonerName}`,
    { next: { revalidate: 60 } }
  );
  const matches: MatchData[] = await response.json();

  return (
    <div className="flex flex-col items-center">
      <User params={params}></User>
      <div className="flex flex-col items-center">
        {matches ? (matches.map((match, index) => (
            <Game key={index} match={match}/>
        ))):(<div className="p-2 bg-white bg-opacity-20 backdrop-blur-md border-2 border-white border-opacity-30 rounded-[10px] overflow-hidden">No matches found</div>)}
      </div>
    </div>
  );
};

export default SummonerPage;
