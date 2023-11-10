export enum StreetType {
  Avenue = 'AVENUE',
  Street = 'STREET',
  Bystreet = 'BYSTREET'
}

export interface Street {
  id: string;
  name: string;
  type: StreetType;
  sidewalks: SidewalkMap[];
  centralWalks: Sidewalk[];
  startWithNames: AdjacentStreet[];
  endWithNames: AdjacentStreet[];
}

export interface AdjacentStreet {
  name: string;
  type: StreetType;
  id: string;
}

export interface SidewalkMap {
  left: Sidewalk[];
  right: Sidewalk[];
}

export interface Sidewalk {
  id: string;
  issues: SidewalkIssue[];
  crosswalks: Crosswalk[];
  widthInCentimeters: number;
  commitIssues: CommitIssue[];
}

export interface User {
  name: string;
  email: string;
}

export interface CommitIssue extends User {
  status: any;
  date: Date;
  issue: string;
}

export enum issueStatusType {
  Processed = 'PROCESSED',
  Inprocessing = 'Inprocessing',
  New = 'NEW'
}

export interface SidewalkIssue {
  borders: SidewalkIssueBarder[];
}

export interface SidewalkIssueBarder {
  heightInCentimeters: number;
  GPS: string;
  commitIssues: CommitIssue[];
}

export interface Crosswalk {
  type: CrosswalkType;
  issues: CrosswalkIssue[];
  benefits: CrosswalkBenefit[];
  GPS: string;
  widthInCentimeters: number;
  direction: CrosswalkDirection;
  commitIssues: CommitIssue[];
}

export enum CrosswalkType {
  Underground = 'UNDERGROUNd',
  Overground = 'OVERGROUNG',
  ByRoad = 'BY_ROAD'
}

export interface CrosswalkIssue {
  borderHeightInCentimeters: number;
  commitIssues: CommitIssue[];
}

export interface CrosswalkBenefit {
  type: CrosswalkBenefitType;
  commitIssues: CommitIssue[];
}

export enum CrosswalkBenefitType {
  Lift = 'LIFT',
  SpecialLift = 'SPECIAL_LIFT',
  SocialWorker = 'SOCIAL_WORKER',
}

export interface CrosswalkDirection {
  direction: CrosswalkDirectionType;
  type: StreetType;
  name: string;
  id: string;
}

export enum CrosswalkDirectionType {
  Lift = 'LIFT',
  Right = 'RIGHT',
  Top = 'TOP',
  Bottom = 'BOTTOM'
}