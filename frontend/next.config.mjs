/** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode: true,
    images: {
      minimumCacheTTL: 3600,
      remotePatterns : [
          {
            protocol: 'http',
            hostname: 'localhost',
            port: '8000',
            pathname: '/static/**',
          },
      ],
    },
  }

export default nextConfig;
