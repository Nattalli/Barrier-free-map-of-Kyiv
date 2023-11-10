import { RouterProvider, Link, createBrowserRouter } from 'react-router-dom';
import './App.css';

function App() {

  const router = createBrowserRouter([
    {
      path: "/",
      element: <div>Hello world! <Link to='/admin'>Your Name</Link></div>,
    },
    {
      path: "/admin",
      element: <div>Hello admin list!</div>,
    },
    {
      path: "/admin/create",
      element: <div>Hello admin create!</div>,
    },
    {
      path: "/admin/:code/edit",
      element: <div>Hello admin edit!</div>,
    },
    {
      path: "/admin/:code",
      element: <div>Hello admin edit!</div>,
    },
    {
      path: "/user",
      element: <div>Hello user list!</div>,
    },
    {
      path: "/user/:code",
      element: <div>Hello user view!</div>,
    },
  ]);

  return (<RouterProvider router={router} />);
}

export default App;
