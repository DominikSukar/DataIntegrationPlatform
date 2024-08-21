import { DM_Sans } from "next/font/google";

import Logo from "@/components/game/Logo";

const dmSans = DM_Sans({
  weight: "400",
  subsets: ["latin"],
});

import { ProfileForm } from "@/components/forms/Form";

const Home = () => {
  return (
    <main className="flex flex-col items-center justify-center min-h-screen">
      <Logo></Logo>
      <ProfileForm></ProfileForm>
    </main>
  );
};

export default Home;
