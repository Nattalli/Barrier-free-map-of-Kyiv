import './admin-street-creator.scss';
import { useNavigate } from 'react-router-dom';
import React, { useState } from 'react';
import Button from 'devextreme-react/button';
import TextBox from 'devextreme-react/text-box';
import SelectBox from 'devextreme-react/select-box';
import { StreetType } from '../../street-type';
import { AdjacentStreet } from '../adjacent-street';

const AdminStreetCreator = () => {
  const navigate = useNavigate();
  const [name, setName] = useState<string>('');
  const [type, setType] = useState<string>('');
  const [startWithNames, setStartWithNames] = useState<AdjacentStreet[]>([{name: null, type: null, id: '0'}]);
  const [endWithNames, setEndWithNames] = useState<AdjacentStreet[]>([{name: null, type: null, id: '0'}]);

  function handleNameChange(event: any) {
    setName(event.value);
  }

  function handleTypeChange(event: any) {
    setType(event.value);
  }

  function addStartWithName() {
    const list = [...startWithNames, {name: null, type: null, id: (startWithNames.length + 1).toString()}];
    setStartWithNames(list);
  }

  function addEndWithName() {
    const list = [...endWithNames, {name: null, type: null, id: (endWithNames.length + 1).toString()}];
    setEndWithNames(list);
  }

  function handleTypeStartWithNameChange(event: any, index: number) {
    const newStartWithNames = startWithNames.map(startWithName => {
      if (startWithName.id === index.toString()) {
        return {...startWithName, type: event.value}
      }
      return startWithName
    });
    setStartWithNames(newStartWithNames);
  }

  function handleNameStartWithNameChange(event: any, index: number) {
    const newStartWithNames = startWithNames.map(startWithName => {
      if (startWithName.id === index.toString()) {
        return {...startWithName, name: event.value}
      }
      return startWithName
    });
    setStartWithNames(newStartWithNames);
  }

  function handleTypeEndWithNameChange(event: any, index: number) {
    const newEndWithNames = endWithNames.map(endWithName => {
      if (endWithName.id === index.toString()) {
        return {...endWithName, type: event.value}
      }
      return endWithName;
    });
    setEndWithNames(newEndWithNames);
  }

  function handleNameEndWithNameChange(event: any, index: number) {
    const newEndWithNames = endWithNames.map(endWithName => {
      if (endWithName.id === index.toString()) {
        return {...endWithName, name: event.value}
      }
      return endWithName;
    });
    setEndWithNames(newEndWithNames);
  }

  function save() {
    navigate('/admin/list')
  }

  return (
    <div className="admin-creator">
      <div className="admin-creator-title">Оцифровати дорогу</div>
      <div className="street-creator-container">
        <div className="label">Назва вулиці</div>
        <TextBox
          className="input"
          value={name}
          placeholder="Напишіть назву"
          onValueChanged={handleNameChange}
          valueChangeEvent='input'
        />
        <div className="label">Тип вулиці</div>
        <SelectBox
          className="input"
          value={type}
          placeholder="Виберіть тип вулиці"
          onValueChanged={handleTypeChange}
          displayExpr="name"
          valueExpr="value"
          items={[{value: StreetType.Street, name: 'Вулиця'}, {value: StreetType.Avenue, name: 'Проспект'}, {value: StreetType.Bystreet, name: 'Провулок'}]}
        />
        <div className="hr-line"></div>
        <div className="label-container">
          <div className="label">Початок вулиці</div>
          <Button onClick={() => addStartWithName()} text="Додати"/>
        </div>
        <div className="input">
          {startWithNames.map((startWithName, index) => <div key={index}>
            <div className="label">Повязана вулиця</div>
            <TextBox
              className="input"
              value={startWithName.name}
              placeholder="Напишіть назву з якої починається вулиця"
              onValueChanged={(e) => handleNameStartWithNameChange(e, index)}
              valueChangeEvent='input'
            />
            <SelectBox
              className="input"
              value={startWithName.type}
              onValueChanged={(e) => handleTypeStartWithNameChange(e, index)}
              placeholder="Виберіть тип з якої починається вулиця"
              displayExpr="name"
              valueExpr="value"
              items={[{value: StreetType.Street, name: 'Вулиця'}, {value: StreetType.Avenue, name: 'Проспект'}, {value: StreetType.Bystreet, name: 'Провулок'}]}
            />
          </div>)}
        </div>
        <div className="hr-line"></div>
        <div className="label-container">
          <div className="label">Кінець вулиці</div>
          <Button onClick={addEndWithName} text="Додати"/>
        </div>
        <div className="input">
          {endWithNames.map((endWithName, index) => <div key={index}>
            <div className="label">Повязана вулиця</div>
            <TextBox
              className="input"
              value={endWithName.name}
              placeholder="Напишіть назву з якої починається вулиця"
              onValueChanged={(e) => handleNameEndWithNameChange(e, index)}
              valueChangeEvent='input'
            />
            <SelectBox
              className="input"
              value={endWithName.type}
              onValueChanged={(e) => handleTypeEndWithNameChange(e, index)}
              placeholder="Виберіть тип з якої починається вулиця"
              displayExpr="name"
              valueExpr="value"
              items={[{value: StreetType.Street, name: 'Вулиця'}, {value: StreetType.Avenue, name: 'Проспект'}, {value: StreetType.Bystreet, name: 'Провулок'}]}
            />
          </div>)}
        </div>
        <Button type='success' onClick={save} text="Зберегти"/>
      </div>
    </div>
  );
}

export default AdminStreetCreator;
