import Logo from "@/components/Logo";
import UserSearch from "@/components/forms/UserSearch";

export default function Home() {
  return (
    <main className="flex flex-col items-center justify-center min-h-screen">
      <Logo></Logo>
      <UserSearch></UserSearch>
    </main>
  );
}
