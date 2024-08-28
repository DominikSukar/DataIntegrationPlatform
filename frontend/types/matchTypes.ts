export interface Participant {
  server: string;
  championId: number;
  championName: string;
  individualPosition: string;
  teamId: number;
  kills: number;
  deaths: number;
  assists: number;
  kda: number;
  summonerName: string;
  tagLine: string;
  items: [number];
  summoners: [number];
  perks: [number];
  vision: number;
  isMain: boolean;
}

export interface MainParticipant extends Participant {
  win: boolean;
  timePlayed: number;
}


export type Result = "Win" | "Defeat" | "Remake";

export interface Info {
  server: string;
  endOfGameResult: string;
  matchId: string;
  gameEndTimestamp: number;
  gameResult: Result;
  gameDuration: number;
  gameMode: string;
  gameType: string;
  teams: Teams;
}

export interface Teams {
  team_1: TeamDetails;
  team_2: TeamDetails;
}

export interface TeamDetails {
  bans: Ban[];
  objectives: Objectives;
}

export interface Ban {
  championId: number;
  pickTurn: number;
}

export interface Objectives {
  baron: ObjectiveDetail;
  champion: ObjectiveDetail;
  dragon: ObjectiveDetail;
  horde: ObjectiveDetail;
  inhibitor: ObjectiveDetail;
  riftHerald: ObjectiveDetail;
  tower: ObjectiveDetail;
}

export interface ObjectiveDetail {
  first: boolean;
  kills: number;
}

export interface MatchData {
  main_participant: MainParticipant;
  team_1: Participant[];
  team_2: Participant[];
  info: Info;
}

export interface SummonerData {
  accountId: string;
  profileIconId: number;
  revisionDate: number;
  id: string;
  puuid: string;
  summonerLevel: number;
  leagueId: string;
  summonerId: string;
  queueType: string;
  tier: string;
  rank: string;
  leaguePoints: number;
  wins: number;
  losses: number;
  winrate: number;
  hotStreak: boolean;
  veteran: boolean;
  freshBlood: boolean;
  inactive: boolean;
}

export interface PageProps {
  params: {
    server: string;
    summonerName: string;
  };
}
