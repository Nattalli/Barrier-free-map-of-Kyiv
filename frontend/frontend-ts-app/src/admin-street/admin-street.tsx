import React, { Component } from 'react';
import './admin-street.scss';
import { Outlet } from 'react-router';
import 'devextreme/dist/css/dx.light.css';
import Button from 'devextreme-react/button';
import { Link } from "react-router-dom";

class AdminStreet extends Component {

  render() {
    return (
      <div className="admin-street">
        <Link to='/admin/create'>
          <Button type='success' text="Create"/>
        </Link>
        <div className="admin-wrapper">
          <Outlet/>
        </div>
      </div>
    );
  }
}

export default AdminStreet;
