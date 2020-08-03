<template>
  <div class='nyancat-wrapper wrapper'>
    <div class='rainbow'>
      <span></span>
    </div>
    <div class='nyan-cat'>
      <div class='feet'></div>
      <div class='tail'>
        <span></span>
      </div>
      <div class='body'></div>
      <div class='head'></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NyanCat',
  mounted: () => {
    let scrollInterval = null;
    scrollInterval = setInterval(() => {
      const parentScrollHeight = document.querySelector('.nyancat-wrapper').parentNode.scrollHeight;
      if (window.pageYOffset >= parentScrollHeight) {
        document.querySelector('.nyancat-wrapper').classList.add('loaded');

        setTimeout(() => {
          const nyancatWrapper = document.querySelector('.nyancat-wrapper');
          nyancatWrapper.classList.remove('loaded');
          nyancatWrapper.style.display = 'none';
        }, 8000);

        clearInterval(scrollInterval);
      }
    }, 200);
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
@function grid ($start, $end, $increment) {
  $str: 0;
  @while $start <= $end {
    @if $start < $end {
      $str: $str + 0 #{$start}#{"px,"};
    }
    @if $start == $end {
      $str: $str + 0 #{$start}#{"px"};
    }
    $start: $start + $increment;
  }
  @return $str;
}

$blue     : $nord0;
$beige    : $nord13;
$pink     : $nord15;
$deeppink : $nord11;
$gray     : $nord15;
$salmon   : $nord12;
$red      : $nord11;
$orange   : $nord12;
$yellow   : $nord13;
$green    : $nord14;
$royalblue: $nord9;
$purple   : $nord10;

body {
  height: 100%;
  overflow: hidden;
}

.sprite {
  position: absolute;
  background: {
    position: grid(0, 125, 5);
    size: 100% 5px;
    repeat: no-repeat;
  }
}

.wrapper {
  overflow: hidden;
  /*position: absolute;
  top: 50%;
  left: 50%;
  width: 400px;
  height: 300px;
  margin-top: -150px;
  margin-left: -200px;
  border-width: 1px;
  overflow: hidden;
  border-style: solid;
  border-color: lighten($blue, 15%);
  background: $blue;
  box-shadow: (0 10px 100px rgba(0,0,0,.3));*/
}

.nyan-cat {
  position: absolute;
  left: -5%;
  top: 30%;
  width: 165px;
  height: 100px;
  margin: {
    top: -50px;
    left: -82px;
  }
  animation: (nyan 400ms step-start infinite);
  transition: all 5s ease-in-out 1s;
}

.body {
  @extend .sprite;
  left: 35px;
  top: 0;
  width: 105px;
  height: 90px;
}

.head {
  @extend .sprite;
  left: 85px;
  top: 25px;
  width: 80px;
  height: 65px;
  animation: (head 400ms linear infinite);
}

.rainbow {
  position: absolute;
  left: 0;
  top: 30%;
  margin-top: -35px;
  width: 0%;
  height: 65px;
  overflow: hidden;
  transition: all 5s ease-in-out 1s;

  span {
    @extend .sprite;
    display: block;
    position: relative;
    top: 0;
    width: 100%;
    height: 130px;
    background: {
      size: 80px 5px;
      repeat: repeat-x;
    }
    animation: (rainbow 400ms step-start infinite);
  }
}

.feet {
  @extend .sprite;
  left: 20px;
  top: 75px;
  width: 120px;
  height: 25px;
  animation: (feet 400ms infinite);
}

.tail {
  position: relative;
  width: 25px;
  height: 30px;
  overflow: hidden;
  top: 30px;
  left: 10px;

  span {
    @extend .sprite;
    width: 25px;
    height: 120px;
    animation: (tail 200ms step-start infinite alternate);
  }
}

.body {
  background-image:
    linear-gradient(to right,
    transparent 0, transparent 10px,
    black 10px, black 95px,
    transparent 95px, transparent 105px),

    linear-gradient(to right,
    transparent 0, transparent 5px,
    black 5px, black 10px,
    $beige 10px, $beige 95px,
    black 95px, black 100px,
    transparent 100px, transparent 105px),

    linear-gradient(to right,
    black 0, black 5px,
    $beige 5px, $beige 20px,
    $pink 20px, $pink 85px,
    $beige 85px, $beige 100px,
    black 100px, black 105px),

    linear-gradient(to right,
    black 0, black 5px,
    $beige 5px, $beige 15px,
    $pink 15px, $pink 45px,
    $deeppink 45px,  $deeppink 50px,
    $pink 50px, $pink 60px,
    $deeppink 60px,  $deeppink 65px,
    $pink 65px, $pink 90px,
    $beige 90px, $beige 100px,
    black 100px, black 105px),

    linear-gradient(to right,
    black 0, black 5px,
    $beige 5px, $beige 10px,
    $pink 10px, $pink 20px,
    $deeppink 20px,  $deeppink 25px,
    $pink 25px, $pink 95px,
    $beige 95px, $beige 100px,
    black 100px, black 105px),
    linear-gradient(to right,
    black 0, black 5px,
    $beige 5px, $beige 10px,
    $pink 10px, $pink 80px,
    $deeppink 80px,  $deeppink 85px,
    $pink 85px, $pink 95px,
    $beige 95px, $beige 100px,
    black 100px, black 105px),
    linear-gradient(to right,
    black 0, black 5px,
    $beige 5px, $beige 10px,
    $pink 10px, $pink 95px,
    $beige 95px, $beige 100px,
    black 100px, black 105px),
    linear-gradient(to right,
    black 0, black 5px,
    $beige 5px, $beige 10px,
    $pink 10px, $pink 40px,
    $deeppink 40px,  $deeppink 45px,
    $pink 45px, $pink 95px,
    $beige 95px, $beige 100px,
    black 100px, black 105px),
    linear-gradient(to right,
    black 0, black 5px,
    $beige 5px, $beige 10px,
    $pink 10px, $pink 95px,
    $beige 95px, $beige 100px,
    black 100px, black 105px),
    linear-gradient(to right,
    black 0, black 5px,
    $beige 5px, $beige 10px,
    $pink 10px, $pink 25px,
    $deeppink 25px,  $deeppink 30px,
    $pink 30px, $pink 95px,
    $beige 95px, $beige 100px,
    black 100px, black 105px),
    linear-gradient(to right,
    black 0, black 5px,
    $beige 5px, $beige 10px,
    $pink 10px, $pink 45px,
    $deeppink 45px,  $deeppink 50px,
    $pink 50px, $pink 95px,
    $beige 95px, $beige 100px,
    black 100px, black 105px),
    linear-gradient(to right,
    black 0, black 5px,
    $beige 5px, $beige 10px,
    $pink 10px, $pink 15px,
    $deeppink 15px,  $deeppink 20px,
    $pink 20px, $pink 95px,
    $beige 95px, $beige 100px,
    black 100px, black 105px),
    linear-gradient(to right,
    black 0, black 5px,
    $beige 5px, $beige 10px,
    $pink 10px, $pink 95px,
    $beige 95px, $beige 100px,
    black 100px, black 105px),
    linear-gradient(to right,
    black 0, black 5px,
    $beige 5px, $beige 10px,
    $pink 10px, $pink 35px,
    $deeppink 35px,  $deeppink 40px,
    $pink 40px, $pink 95px,
    $beige 95px, $beige 100px,
    black 100px, black 105px),

    linear-gradient(to right,
    black 0, black 5px,
    $beige 5px, $beige 15px,
    $pink 15px, $pink 20px,
    $deeppink 20px,  $deeppink 25px,
    $pink 25px, $pink 90px,
    $beige 90px, $beige 100px,
    black 100px, black 105px),

    linear-gradient(to right,
    black 0, black 5px,
    $beige 5px, $beige 20px,
    $pink 20px, $pink 85px,
    $beige 85px, $beige 100px,
    black 100px, black 105px),

    linear-gradient(to right,
    transparent 0, transparent 5px,
    black 5px, black 10px,
    $beige 10px, $beige 95px,
    black 95px, black 100px,
    transparent 100px, transparent 105px),

    linear-gradient(to right,
    transparent 0, transparent 10px,
    black 10px, black 95px,
    transparent 95px, transparent 105px)
  ;
}

.head {
  background-image:
    linear-gradient(to right,
    transparent 0, transparent 10px,
    black 10px, black 20px,
    transparent 20px, transparent 60px,
    black 60px, black 70px,
    transparent 70px, transparent 105px),

    linear-gradient(to right,
    transparent 0, transparent 5px,
    black 5px, black 10px,
    $gray 10px, $gray 20px,
    black 20px, black 25px,
    transparent 25px, transparent 55px,
    black 55px, black 60px,
    $gray 60px, $gray 70px,
    black 70px, black 75px,
    transparent 75px, transparent 80px),

    linear-gradient(to right,
    transparent 0, transparent 5px,
    black 5px, black 10px,
    $gray 10px, $gray 25px,
    black 25px, black 30px,
    transparent 30px, transparent 50px,
    black 50px, black 55px,
    $gray 55px, $gray 70px,
    black 70px, black 75px,
    transparent 75px, transparent 80px),

    linear-gradient(to right,
    transparent 0, transparent 5px,
    black 5px, black 10px,
    $gray 10px, $gray 30px,
    black 30px, black 35px,
    black 35px, black 50px,
    $gray 50px, $gray 70px,
    black 70px, black 75px,
    transparent 75px, transparent 80px),

    linear-gradient(to right,
    transparent 0, transparent 5px,
    black 5px, black 10px,
    $gray 10px, $gray 70px,
    black 70px, black 75px,
    transparent 75px, transparent 80px),

    linear-gradient(to right,
    black 0, black 5px,
    $gray 5px, $gray 75px,
    black 75px, black 80px),

    linear-gradient(to right,
    black 0, black 5px,
    $gray 5px, $gray 20px,
    white 20px, white 25px,
    black 25px, black 30px,
    $gray 30px, $gray 55px,
    white 55px, white 60px,
    black 60px, black 65px,
    $gray 65px, $gray 75px,
    black 75px, black 80px),

    linear-gradient(to right,
    black 0, black 5px,
    $gray 5px, $gray 20px,
    black 20px, black 30px,
    $gray 30px, $gray 45px,
    black 45px, black 50px,
    $gray 50px, $gray 55px,
    black 55px, black 65px,
    $gray 65px, $gray 75px,
    black 75px, black 80px),

    linear-gradient(to right,
    black 0, black 5px,
    $gray 5px, $gray 10px,
    $salmon 10px, $salmon 20px,
    $gray 20px, $gray 65px,
    $salmon 65px, $salmon 75px,
    black 75px, black 80px),

    linear-gradient(to right,
    black 0, black 5px,
    $gray 5px, $gray 10px,
    $salmon 10px, $salmon 20px,
    $gray 20px, $gray 25px,
    black 25px, black 30px,
    $gray 30px, $gray 40px,
    black 40px, black 45px,
    $gray 45px, $gray 55px,
    black 55px, black 60px,
    $gray 60px, $gray 65px,
    $salmon 65px, $salmon 75px,
    black 75px, black 80px),

    linear-gradient(to right,
    transparent 0, transparent 5px,
    black 5px, black 10px,
    $gray 10px, $gray 25px,
    black 25px, black 60px,
    $gray 60px, $gray 70px,
    black 70px, black 75px,
    transparent 75px, transparent 80px),

    linear-gradient(to right,
    transparent 0, transparent 10px,
    black 10px, black 15px,
    $gray 15px, $gray 65px,
    black 65px, black 70px,
    transparent 70px, transparent 80px),

    linear-gradient(to right,
    transparent 0, transparent 15px,
    black 15px, black 65px,
    transparent 65px, transparent 80px)
  ;
}

.rainbow > span {
  background-image:
    linear-gradient(to right,
    $red 0, $red 50%,
    transparent 50%, transparent 100%),
    linear-gradient(to right,
    $red 0, $red 100%),

    linear-gradient(to right,
    $orange 0, $orange 50%,
    $red 50%, $red 100%),
    linear-gradient(to right,
    $orange 0, $orange 100%),

    linear-gradient(to right,
    $yellow 0, $yellow 50%,
    $orange 50%, $orange 100%),
    linear-gradient(to right,
    $yellow 0, $yellow 100%),

    linear-gradient(to right,
    $green 0, $green 50%,
    $yellow 50%, $yellow 100%),
    linear-gradient(to right,
    $green 0, $green 100%),

    linear-gradient(to right,
    $royalblue 0, $royalblue 50%,
    $green 50%, $green 100%),
    linear-gradient(to right,
    $royalblue 0, $royalblue 100%),

    linear-gradient(to right,
    $purple 0, $purple 50%,
    $royalblue 50%, $royalblue 100%),
    linear-gradient(to right,
    $purple 0, $purple 100%),

    linear-gradient(to right,
    transparent 0, transparent 50%,
    $purple 50%, $purple 100%),

    linear-gradient(to right,
    transparent 0, transparent 50%,
    $red 50%, $red 100%),
    linear-gradient(to right,
    $red 0, $red 100%),

    linear-gradient(to right,
    $red 0, $red 50%,
    $orange 50%, $orange 100%),
    linear-gradient(to right,
    $orange 0, $orange 100%),

    linear-gradient(to right,
    $orange 0, $orange 50%,
    $yellow 50%, $yellow 100%),
    linear-gradient(to right,
    $yellow 0, $yellow 100%),

    linear-gradient(to right,
    $yellow 0, $yellow 50%,
    $green 50%, $green 100%),
    linear-gradient(to right,
    $green 0, $green 100%),

    linear-gradient(to right,
    $green 0, $green 50%,
    $royalblue 50%, $royalblue 100%),
    linear-gradient(to right,
    $royalblue 0, $royalblue 100%),

    linear-gradient(to right,
    $royalblue 0, $royalblue 50%,
    $purple 50%, $purple 100%),
    linear-gradient(to right,
    $purple 0, $purple 100%),

    linear-gradient(to right,
    $purple 0, $purple 50%,
    transparent 50%, transparent 100%)
  ;
}

.feet {
  background-image:
    linear-gradient(to right,
    transparent 0, transparent 10px,
    black 10px, black 25px,
    transparent 25px, transparent 120px),

    linear-gradient(to right,
    transparent 0, transparent 5px,
    black 5px, black 10px,
    $gray 10px, $gray 110px,
    transparent 110px, transparent 120px),

    linear-gradient(to right,
    black 0, black 5px,
    $gray 5px, $gray 20px,
    black 20px, black 35px,
    $gray 35px, $gray 40px,
    black 40px, black 80px,
    $gray 80px, $gray 110px,
    black 110px, black 115px,
    transparent 115px, transparent 120px),

    linear-gradient(to right,
    black 0, black 5px,
    $gray 5px, $gray 15px,
    black 15px, black 20px,
    transparent 20px, transparent 25px,
    black 25px, black 30px,
    $gray 30px, $gray 40px,
    black 40px, black 45px,
    transparent 45px, transparent 75px,
    black 75px, black 80px,
    $gray 80px, $gray 90px,
    black 90px, black 95px,
    transparent 95px, transparent 100px,
    black 100px, black 105px,
    $gray 105px, $gray 115px,
    black 115px, black 120px),

    linear-gradient(to right,
    black 0, black 15px,
    transparent 15px, transparent 30px,
    black 30px, black 45px,
    transparent 45px, transparent 80px,
    black 80px, black 95px,
    transparent 95px, transparent 105px,
    black 105px, black 120px)
  ;
}

.tail > span {
  background-image:
    linear-gradient(to right,
    transparent 0, transparent 5px,
    black 5px, black 15px,
    transparent 15px),
    linear-gradient(to right,
    black 0, black 5px,
    $gray 5px, $gray 15px,
    black 15px, black 20px,
    transparent 20px),
    linear-gradient(to right,
    black 0, black 5px,
    $gray 5px, $gray 15px,
    black 15px),
    linear-gradient(to right,
    transparent 0, transparent 5px,
    black 5px, black 10px,
    $gray 10px),
    linear-gradient(to right,
    transparent 0, transparent 10px,
    black 10px, black 20px,
    $gray 20px),
    linear-gradient(to right,
    transparent 0, transparent 15px,
    black 15px),

    linear-gradient(to right,
    transparent 0, transparent 100%),
    linear-gradient(to right,
    transparent 0, transparent 5px,
    black 5px, black 20px,
    transparent 20px),
    linear-gradient(to right,
    black 0, black 5px,
    $gray 5px, $gray 15px,
    black 15px),
    linear-gradient(to right,
    black 0, black 10px,
    $gray 10px, $gray 25px),
    linear-gradient(to right,
    transparent 0, transparent 10px,
    black 10px, black 20px,
    $gray 20px),
    linear-gradient(to right,
    transparent 0, transparent 20px,
    black 20px),

    linear-gradient(to right,
    transparent 0, transparent 100%),
    linear-gradient(to right,
    transparent 0, transparent 20px,
    black 20px),
    linear-gradient(to right,
    transparent 0, transparent 10px,
    black 10px),
    linear-gradient(to right,
    transparent 0, transparent 5px,
    black 5px, black 10px,
    $gray 10px),
    linear-gradient(to right,
    black 0, black 5px,
    $gray 5px, $gray 20px,
    black 20px),
    linear-gradient(to right,
    transparent 0, transparent 5px,
    black 5px),

    linear-gradient(to right,
    transparent 0, transparent 20px,
    black 20px),
    linear-gradient(to right,
    transparent 0, transparent 15px,
    black 15px, black 20px,
    $gray 20px),
    linear-gradient(to right,
    transparent 0, transparent 10px,
    black 10px, black 15px,
    $gray 15px),
    linear-gradient(to right,
    transparent 0, transparent 5px,
    black 5px, black 10px,
    $gray 10px, $gray 20px,
    black 20px),
    linear-gradient(to right,
    black 0, black 5px,
    $gray 5px, $gray 15px,
    black 15px),
    linear-gradient(to right,
    transparent 0, transparent 5px,
    black 5px, black 15px,
    transparent 15px)
  ;
}

.star > span {
  background-image:
    linear-gradient(to right,
    transparent 0, transparent 12px,
    white 12px, white 16px,
    transparent 16px, transparent 112px),
    linear-gradient(to right,
    transparent 0, transparent 12px,
    white 12px, white 16px,
    transparent 16px, transparent 112px),

    linear-gradient(to right,
    transparent 0, transparent 4px,
    white 4px, white 8px,
    transparent 8px, transparent 20px,
    white 20px, white 24px,
    transparent 24px, transparent 40px,
    white 40px, white 44px,
    transparent 44px, transparent 68px,
    white 68px, white 72px,
    transparent 72px, transparent 112px),
    linear-gradient(to right,
    transparent 0, transparent 4px,
    white 4px, white 8px,
    transparent 8px, transparent 20px,
    white 20px, white 24px,
    transparent 24px, transparent 40px,
    white 40px, white 44px,
    transparent 44px, transparent 68px,
    white 68px, white 72px,
    transparent 72px, transparent 112px),

    linear-gradient(to right,
    transparent 0, transparent 68px,
    white 68px, white 72px,
    transparent 72px, transparent 112px),
    linear-gradient(to right,
    transparent 0, transparent 68px,
    white 68px, white 72px,
    transparent 72px, transparent 112px),

    linear-gradient(to right,
    white 0, white 4px,
    transparent 4px, transparent 24px,
    white 24px, white 28px,
    transparent 28px, transparent 32px,
    white 32px, white 36px,
    transparent 36px, transparent 40px,
    white 40px, white 44px,
    transparent 44px, transparent 48px,
    white 48px, white 52px,
    transparent 52px, transparent 60px,
    white 60px, white 68px,
    transparent 68px, transparent 72px,
    white 72px, white 80px,
    transparent 80px, transparent 96px,
    white 96px, white 100px,
    transparent 100px, transparent 112px),
    linear-gradient(to right,
    white 0, white 4px,
    transparent 4px, transparent 24px,
    white 24px, white 28px,
    transparent 28px, transparent 32px,
    white 32px, white 36px,
    transparent 36px, transparent 40px,
    white 40px, white 44px,
    transparent 44px, transparent 48px,
    white 48px, white 52px,
    transparent 52px, transparent 60px,
    white 60px, white 68px,
    transparent 68px, transparent 72px,
    white 72px, white 80px,
    transparent 80px, transparent 96px,
    white 96px, white 100px,
    transparent 100px, transparent 112px),

    linear-gradient(to right,
    transparent 0, transparent 68px,
    white 68px, white 72px,
    transparent 72px, transparent 112px),
    linear-gradient(to right,
    transparent 0, transparent 68px,
    white 68px, white 72px,
    transparent 72px, transparent 112px),

    linear-gradient(to right,
    transparent 0, transparent 4px,
    white 4px, white 8px,
    transparent 8px, transparent 20px,
    white 20px, white 24px,
    transparent 24px, transparent 40px,
    white 40px, white 44px,
    transparent 44px, transparent 68px,
    white 68px, white 72px,
    transparent 72px, transparent 112px),
    linear-gradient(to right,
    transparent 0, transparent 4px,
    white 4px, white 8px,
    transparent 8px, transparent 20px,
    white 20px, white 24px,
    transparent 24px, transparent 40px,
    white 40px, white 44px,
    transparent 44px, transparent 68px,
    white 68px, white 72px,
    transparent 72px, transparent 112px),

    linear-gradient(to right,
    transparent 0, transparent 12px,
    white 12px, white 16px,
    transparent 16px, transparent 112px),
    linear-gradient(to right,
    transparent 0, transparent 12px,
    white 12px, white 16px,
    transparent 16px, transparent 112px)
  ;
}

.loaded {
  .nyan-cat {
    left: 95%;
    transition: all 2s ease 1s;
  }

  .rainbow {
    width: 95%;
    transition: all 2.1s ease 1s;
  }
}

@keyframes rainbow {
  0%   {top: 0}
  50%  {top: 0}
  100% {top: -65px}
}

@keyframes moveleft {
  0%   {left: 0}
  100% {left: -400px}
}

@keyframes star {
  0%        {left: 0}
  25%       {left: 0}
  49.99%    {left: 0}
  50%       {left: -28px}
  74.99%    {left: -28px}
  75%       {left: -56px}
  99.99%    {left: -56px}
  100%      {left: -84px}
}

@keyframes nyan {
  0%    {margin-top: -50px}
  10%   {margin-top: -50px}
  80%   {margin-top: -53px}
  100%  {margin-top: -50px}
}

@keyframes feet {
  0%    {left: 20px}
  100%  {left: 30px}
}

@keyframes head {
  0%      {top: 25px; left: 85px}
  24.99%  {top: 25px; left: 85px}
  25%     {top: 22px; left: 88px}
  49.99%  {top: 22px; left: 88px}
  50%     {top: 22px; left: 85px}
  74.99%  {top: 22px; left: 85px}
  75%     {top: 22px; left: 82px}
  99.99%  {top: 22px; left: 82px}
  100%    {top: 25px; left: 85px}
}

@keyframes tail {
  0%        {top: 0}
  25%       {top: 0}
  49.99%    {top: 0}
  50%       {top: -30px}
  74.99%    {top: -30px}
  75%       {top: -60px}
  99.99%    {top: -60px}
  100%      {top: -90px}
}

</style>
