create schema if not exists "authentication";

alter table "authentication"."session" add column "activeOrganizationId" text;

create table "authentication"."organization" ("id" text not null primary key, "name" text not null, "slug" text not null unique, "logo" text, "createdAt" timestamptz not null, "metadata" text);

create table "authentication"."member" ("id" text not null primary key, "organizationId" text not null references "authentication"."organization" ("id") on delete cascade, "userId" text not null references "authentication"."user" ("id") on delete cascade, "role" text not null, "createdAt" timestamptz not null);

create table "authentication"."invitation" ("id" text not null primary key, "organizationId" text not null references "authentication"."organization" ("id") on delete cascade, "email" text not null, "role" text, "status" text not null, "expiresAt" timestamptz not null, "createdAt" timestamptz default CURRENT_TIMESTAMP not null, "inviterId" text not null references "authentication"."user" ("id") on delete cascade);

create index "member_organizationId_idx" on "authentication"."member" ("organizationId");

create index "member_userId_idx" on "authentication"."member" ("userId");

create index "invitation_organizationId_idx" on "authentication"."invitation" ("organizationId");

create index "invitation_email_idx" on "authentication"."invitation" ("email");