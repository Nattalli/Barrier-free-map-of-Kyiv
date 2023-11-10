import { RouterProvider, Link, createBrowserRouter, Outlet } from 'react-router-dom';
import './App.scss';
import AdminStreetList from './admin-street/list/admin-street-list';
import AdminStreet from './admin-street/admin-street';

function App() {
  const router = createBrowserRouter([
    {
      path: "/",
      element: <div>
        <div className="menu-container">
          <Link className="link" to="/admin/list">Admin</Link>
          <Link className="link" to="/user/list">User</Link>
        </div>
        <div className="wrapper">
          <Outlet/>
        </div>
      </div>,
      children: [
        {
          path: "/admin",
          element: <AdminStreet/>,
          children: [
            {
              path: "list",
              element: <AdminStreetList/>,
            },
            {
              path: "create",
              element: <div>Hello admin create!</div>,
            },
            {
              path: ":code/edit",
              element: <div>Hello admin edit!</div>,
            },
            {
              path: ":code",
              element: <div>Hello admin edit!</div>,
            }
          ]
        },
        {
          path: "/user",
          element: <div>Hello user list!</div>,
          children: [
            {
              path: "list",
              element: <div>Hello user view!</div>,
            },
            {
              path: ":code",
              element: <div>Hello user view!</div>,
            }
          ]
        }
      ]
    }
  ]);

  return (
    <RouterProvider router={router}/>
  );
}

export default App;
