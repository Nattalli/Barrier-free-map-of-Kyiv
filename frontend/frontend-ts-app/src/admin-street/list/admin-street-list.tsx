import { Component } from 'react';
import './admin-street-list.scss';
import DataGrid, {
  Column,
  Pager,
  Paging,
  SearchPanel,
} from 'devextreme-react/data-grid';
import { ListableStreet } from './listable-street';
import { StreetType } from '../../street-type';

class AdminStreetList extends Component {

  dataSourceStreets: ListableStreet[] = [
    {
      id: '0',
      name: 'Pchilka',
      type: StreetType.Avenue,
      criationDate: new Date()
    }
  ];

  componentDidMount() {
  }

  render() {
    return (
      <DataGrid
        dataSource={this.dataSourceStreets}
        allowColumnReordering={true}
        rowAlternationEnabled={true}
        showBorders={true}
        width="100%">
        <SearchPanel visible={true}/>
        <Column dataField="name" dataType="string"/>
        <Column dataField="criationDate" dataType="date"/>
        <Column dataField="type" dataType="string"/>
        <Pager allowedPageSizes={[10, 25, 50, 100]} showPageSizeSelector={true}/>
        <Paging defaultPageSize={10}/>
      </DataGrid>
    );
  }
}

export default AdminStreetList;
