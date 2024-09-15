import { DM_Sans } from "next/font/google";

import Logo from "@/components/Logo";
import UserSearch from "@/components/forms/UserSearch";

const dmSans = DM_Sans({
  weight: "400",
  subsets: ["latin"],
});


export default function Home() {
  return (
    <main className="flex flex-col items-center justify-center min-h-screen">
      <Logo></Logo>
      <UserSearch></UserSearch>
    </main>
  );
};
