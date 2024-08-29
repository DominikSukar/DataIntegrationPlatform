import GameDetailsParticipant from "./GameDetailsParticipant";

import { Participant, Info } from "@/types/matchTypes";

const GameDetails = async ({
  team_1,
  team_2,
  info,
}: {
  team_1: Participant[];
  team_2: Participant[];
  info: Info;
}) => {
  return (
    <div className="flex justify-center gap-20 mt-5">
      <div>
      <h2 className="text-center text-red-500">Red team</h2>
        {team_1.map((participant, index) => (
          <GameDetailsParticipant key={index} participant={participant} info={info} />
        ))}
        {/*Bans DPS DPSTAKEN GOLD TOWERS DRAGONS BARON KRUGS HERALDS */}
      </div>
      <div>
        {/* Bans DPS DPSTAKEN GOLD TOWERS DRAGONS BARON KRUGS HERALDS */}
        <h2 className="text-center text-blue-500">Blue team</h2>
        {team_2.map((participant, index) => (
          <GameDetailsParticipant key={index} participant={participant} info={info} isReversed={true} />
        ))}
      </div>
    </div>
  );
};

export default GameDetails;
