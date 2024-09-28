import ProfileIcon from "@/components/icons/serverSide/ProfileIcon";
import RankIcon from "@/components/icons/serverSide/RankIcon";

import { DOMAIN } from "@/constants/api";
import { PageProps, SummonerData } from "@/types/matchTypes";

export default async function User({ params }: PageProps) {
  const server = params.server;
  const summonerName = params.summonerName;

  const response = await fetch(
    `${DOMAIN}/summoner/${server}/?summoner_name=${summonerName}`,
    { next: { revalidate: 3600 } }
  );

  const user: SummonerData = await response.json();

  return (
    <div className="lg:flex items-center place-content-between text-white border border-white bg-white bg-opacity-20 backdrop-blur-md mb-28 mt-10">
      <div className="flex items-center">
        <ProfileIcon iconID={user.profileIconId} size={120}></ProfileIcon>
        <div className="flex flex-col">
          <h1 className="font-bold m-2 md:text-xl sm:text-lg">
            {params.summonerName}
          </h1>
          <h3 className="font-bold m-2">Level {user.summonerLevel}</h3>
        </div>
      </div>
      <div className="flex mr-16">
        {user.tier ? (
          <>
            <RankIcon rankName={user.tier} size={120}></RankIcon>
            <div className="flex flex-col items-center justify-center">
              <div className="flex">
                {user.tier} {user.rank}{" "}
                <div className="text-slate-400 ml-2">
                  {user.leaguePoints} LP
                </div>
              </div>
              <div className="flex">
                <p className="text-green-600">{user.wins}W</p>
                <p className="ml-1 text-red-600">{user.losses}L </p>
                <div className="text-slate-400 ml-2">{user.winrate} % WR</div>
              </div>
            </div>
          </>
        ) : (
          <>
            <div className="flex flex-col items-center justify-center">
              <p>UNRANKED</p>
              <div className="flex">
                <p className="text-green-600">0W</p>
                <p className="ml-1 text-red-600">0L </p>
                <div className="text-slate-400 ml-2">0 % WR</div>
              </div>
            </div>
          </>
        )}
      </div>
    </div>
  );
}
