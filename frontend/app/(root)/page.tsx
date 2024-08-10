import { DM_Sans } from 'next/font/google'

const dmSans = DM_Sans({
  weight: '400',
  subsets: ['latin'],
})

import { ProfileForm } from "@/components/forms/Form"

const Home = () => {
  return (
    <main className="flex flex-col items-center justify-center min-h-screen">
      <div className="text-7xl m-6 backdrop-blur-md backdrop-brightness-75 select-none">FF15.GG</div>
      <ProfileForm></ProfileForm>
    </main>
  )
}

export default Home