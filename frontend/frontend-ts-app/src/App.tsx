import { RouterProvider, Link, createBrowserRouter, Outlet } from 'react-router-dom';
import './App.scss';
import AdminStreetList from './admin-street/list/admin-street-list';
import AdminStreet from './admin-street/admin-street';
import { MainPage } from './MainPage';

function App() {
  const router = createBrowserRouter([
    {
      path: "/",
      element: <div className="content">
        <div className="menu-container">
          <div className="wrapper">
            <Link className="link" to="/admin/list">Адміністратор</Link>
            <Link className="link" to="/user">Користувач</Link>
          </div>
        </div>
        <div className="wrapper wrapper-padding">
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
          element: <MainPage/>,
        }
      ]
    }
  ]);

  return (
    <RouterProvider router={router}/>
  );
}

export default App;
