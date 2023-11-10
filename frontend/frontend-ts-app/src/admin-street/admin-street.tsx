import React, { Component } from 'react';
import './admin-street.scss';
import { Outlet } from 'react-router';
import { Link } from 'react-router-dom';

class AdminStreet extends Component {

  render() {
    return (
      <div className="admin-street">
        <Link className="button-link" to="/admin/create">Create</Link>
        <div className="admin-wrapper">
          <Outlet/>
        </div>
      </div>
    );
  }
}

export default AdminStreet;
