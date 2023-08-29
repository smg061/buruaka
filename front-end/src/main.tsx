import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import Login from './pages/login'

import './index.css'
import Navbar from './components/Navbar.tsx'
import {
  createBrowserRouter,
  Outlet,
  RouterProvider,
} from "react-router-dom";
import {
  useQuery,
  useMutation,
  useQueryClient,
  QueryClient,
  QueryClientProvider,
} from '@tanstack/react-query'
import Momotalk from './pages/momotalk/index.tsx'

const queryClient = new QueryClient()

function NavbarWrapper() {
  return (
    <div >
      <Navbar />
      <main >
        <Outlet />
      </main>
    </div>
  )
}
const router = createBrowserRouter([
  {
    path: "/",
    element: <NavbarWrapper />,
    children: [
      {
        path: "/",
        element: <Momotalk />,
        
      },
      {
        path: "/login",
        element: <Login />,
      },
      {
        path: "/momotalk",
        element: <Momotalk />,
      }
    ],
  },
]);
ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
    <RouterProvider router={router} />
    </QueryClientProvider>
  </React.StrictMode>,
)
