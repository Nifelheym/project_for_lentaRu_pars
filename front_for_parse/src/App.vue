<template>
<!-- eslint-disable -->
  <div id="app">
    <table class="tableNews">
      <thead>
        <tr>
          <th>Дата</th>
          <th>Новость</th>
          <th>Категория</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(n, index) in param" class="row-of-table" >
          <td class="tableDate" :id='index' @click='showSelectMenu(index,"tableDate",counterOfCLick)'>{{n.date}}</td>
          <td class="tableNews" :id='index' @click='showSelectMenu(index, "tableNews",counterOfCLick)'>{{n.news}}</td>
          <td class="tableALT" :id='index' @click='showSelectMenu(index, "tableALT",counterOfCLick)'>{{n.alt}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios';

export default {
  name: 'App',
  data () {
    return {
      param: [],
      counterOfCLick: 0
    }
  },
  methods: {
    showSelectMenu: function (index, classname, counter) {
      let massivOfClasses = document.getElementsByClassName(classname);
      classname === 'tableNews'? index++ : index
      this.counterOfCLick ++
      switch (counter) {
      case 0:
        massivOfClasses[index].style.backgroundColor= 'blue'
        break
      case 1:
        massivOfClasses[index].style.backgroundColor= 'green'
        break
      case 2:
        massivOfClasses[index].style.backgroundColor= 'red'
        break
      case 3:
        massivOfClasses[index].style.backgroundColor= 'white'
        break
      default:
        massivOfClasses[index].style.backgroundColor= 'black'
        this.counterOfCLick = 0;
        break
    }

    }
  },
  mounted: function getnews() {
    axios.get('/static/news.json')
      .then(res => {
        this.param = res.data;
      });
  }
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  font-size: 20px;
}
table.tableNews {
  border: 2px solid #141414;
}
tr.row-of-table {

  border: 2px solid #141414;

}
td.tableDate {
 border: 2px solid #141414;
 height: 2em;
 width: 2em;
}
td.tableNews {
  border: 2px solid #141414;
}
td.tableALT {
  border: 2px solid #141414;
}
/* .whitebg{
    background:white
    }
 .graybg{
    background:green
 } */
</style>
