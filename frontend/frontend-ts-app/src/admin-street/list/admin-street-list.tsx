import './admin-street-list.scss';
import DataGrid, {
  Column,
  Pager,
  Paging,
  SearchPanel,
} from 'devextreme-react/data-grid';
import { ListableStreet } from './listable-street';
import { StreetType } from '../../street-type';
import { Link, useNavigate } from 'react-router-dom';
import React from 'react';
import Button from 'devextreme-react/button';

const dataSourceStreets: ListableStreet[] = [
  {
    id: '0',
    name: 'Pchilka',
    type: StreetType.Avenue,
    criationDate: new Date()
  }
];

const AdminStreetList = () => {
  const navigate = useNavigate();

  function handleRowClick() {
    navigate('/admin/create')
  }

  return (
    <div>
      <div className="admin-list-title">Оцифровані дороги</div>
      <Link to='/admin/create'>
        <Button type='success' text="Створити"/>
      </Link>
      <div className="digitized-street">
        <DataGrid
          dataSource={dataSourceStreets}
          allowColumnReordering={true}
          rowAlternationEnabled={true}
          showBorders={true}
          onRowClick={handleRowClick}
          width="100%">
          <SearchPanel visible={true}/>
          <Column dataField="criationDate" caption="Дата створення" dataType="date"/>
          <Column dataField="name" caption="Назва вулиці" dataType="string"/>
          <Column dataField="type"caption="Тип Вулиці" dataType="string"/>
          <Pager allowedPageSizes={[10, 25, 50, 100]} showPageSizeSelector={true}/>
          <Paging defaultPageSize={10}/>
        </DataGrid>
      </div>
    </div>
    );
}

export default AdminStreetList;
