import React, { Component } from 'react';
import './admin-street.scss';
import { Outlet } from 'react-router';
import 'devextreme/dist/css/dx.light.css';

class AdminStreet extends Component {

  render() {
    return (
      <div className="admin-street">
        <div className="admin-wrapper">
          <Outlet/>
        </div>
      </div>
    );
  }
}

export default AdminStreet;
