import { StreetType } from '../../street-type';

export interface ListableStreet {
  id: string;
  name: string;
  type: StreetType;
  criationDate: Date;
}