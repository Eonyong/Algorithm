// 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
// 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
function solution(s){
  var result = true;
  var Tp=0, Tt=0;
  for(var i=0;i<s.length;i++){
    if(s[i]=='P'){
      Tp+=1;
    }
    else if(s[i]=='Y'){
      Tt+=1;
    }
    else if(s[i]=='p'){
      Tp+=1;
    }
    else if(s[i]=='y'){
      Tt+=1;
    }
  }
    return Tp==Tt;

}