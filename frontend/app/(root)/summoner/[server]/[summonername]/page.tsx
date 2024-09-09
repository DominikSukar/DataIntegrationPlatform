import User from "./User";
import Game from "./Game";

import Logo from "@/components/Logo";
import ProfileForm from "@/components/forms/Form";

import { MatchData, PageProps } from "@/types/matchTypes";
import { DOMAIN } from "@/constants/api";

const SummonerPage = async ({ params }: PageProps) => {
  const { server, summonerName } = params;

  const response = await fetch(
    `${DOMAIN}/match_history/${server}/?summoner_name=${summonerName}`,
    { next: { revalidate: 60 } }
  );
  if (!response.ok) {
    return (
      <div className="flex flex-col items-center justify-center min-h-screen">
          <div className="p-5 bg-white bg-opacity-20 backdrop-blur-md border-2 border-white border-opacity-30 rounded-[10px] overflow-hidden text-center">
            <h1 className="flex justify-center">
              <p>User</p>
              <p className="ml-1 text-red-600">{summonerName}</p>
              <p className="ml-1">not found</p>
              </h1>
            <h3 className="flex justify-center">
              <p className="text-red-600">{response.status}</p>
              <p className="ml-1">{response.statusText}</p>
            </h3>
          </div>
          <div className="flex flex-col items-center justify-center">
            <Logo></Logo>
            <ProfileForm></ProfileForm>
          </div>
      </div>
    );
  }
  const matches: MatchData[] = await response.json();

  return (
    <div className="flex flex-col items-center">
      <User params={params}></User>
      <div className="flex flex-col items-center">
        {matches.length ? (matches.map((match, index) => (
            <Game key={index} match={match}/>
        ))):(<div className="p-2 bg-white bg-opacity-20 backdrop-blur-md border-2 border-white border-opacity-30 rounded-[10px] overflow-hidden">No ranked 5x5 matches found</div>)}
      </div>
    </div>
  );
};

export default SummonerPage;
