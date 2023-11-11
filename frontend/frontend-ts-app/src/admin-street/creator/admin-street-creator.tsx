import './admin-street-creator.scss';
import { useNavigate } from 'react-router-dom';
import React from 'react';
import Button from 'devextreme-react/button';
import TextBox from 'devextreme-react/text-box';
import SelectBox from 'devextreme-react/select-box';
import { StreetType } from '../../street-type';

const AdminStreetCreator = () => {
  const navigate = useNavigate();

  function handleNameChange(event: any) {
    street.name = event.value;
    console.log(event,street)
  }

  function handleTypeChange(event: any) {
    street.type = event.value;
    console.log(event,street)
  }

  const street = {
    name: '',
    type: ''
  };




  return (
    <div>
      <div className="admin-creator-title">Оцифровати дорогу</div>
      <div className="street-creator-container">
        <div className="label">Назва вулиці</div>
        <TextBox
          className="input"
          value={street.name}
          onValueChanged={(e) => handleNameChange(e)}
          valueChangeEvent='input'
        />
        <div className="label">Тип вулиці</div>
        <SelectBox
          className="input"
          value={street.type}
          onValueChanged={(e) => handleTypeChange(e)}
          displayExpr="name"
          valueExpr="value"
          items={[{value: StreetType.Street, name: 'Вулиця'}, {value: StreetType.Avenue, name: 'Проспект'}, {value: StreetType.Bystreet, name: 'Провулок'}]}
        />
        <Button type='success' text="Зберегти"/>
      </div>
    </div>
  );
}

export default AdminStreetCreator;
