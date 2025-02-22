select dt,temp,feels_like,temp - feel_like as diff

from {{ref("temp_greater_than_35")}}
where feels_like is not null