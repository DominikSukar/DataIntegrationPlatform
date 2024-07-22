import { cookies } from "next/headers";

import { Button } from "@/components/ui/button"
import { ProfileForm } from "@/components/Form"

const Home = () => {
  const cookieStore = cookies();
  return (
    <main className="flex flex-col items-center justify-center min-h-screen">
      <div className="text-7xl m-6 backdrop-blur-md backdrop-brightness-75">FF15.GG</div>
      <ProfileForm></ProfileForm>
    </main>
  )
}

export default Home