import { StreetType } from '../../street-type';

export interface Street {
  id: string;
  name: string;
  type: StreetType;
  criationDate: Date;
}