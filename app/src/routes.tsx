import { createBrowserRouter } from 'react-router-dom'
import Home from './pages/home'
import DefaultLayout from './layouts/default'
import Projects from './pages/projects'

const routes = [
  {
    path: '/',
    element: <DefaultLayout />,
    children: [
      { 
        path: '/',
        element: <Home />,
      },
      {
        path: '/projects',
        element: <Projects />,
      }
    ]
  }

]

export const AppRouter = createBrowserRouter(routes)
