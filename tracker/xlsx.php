<!--
     Author: Krzysztof Hrybacz <krzysztof@zygtech.pl>
     License: GNU General Public License -- version 3
-->
<?php
	require_once('config.php');
	require_once('SimpleXLSXGen.php');
	if ($_GET['id']!='') {
		$excel=[['Date','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00']];
		$lines=file($installdir . '/places/' . $_GET['id'] . '.txt');
		$l=intval(substr(explode(' ',$lines[0])[1],0,2));
		$row=array();
		for ($i=0;$i<$l-10;$i++)
				$row[]=0;
		foreach ($lines as $line) {
			$row[]=intval(substr(explode(' ',$line)[2],0,strlen(explode(' ',$line)[2])-1));
			$l++;
			if ($l==21) {
				array_unshift($row,explode(' ',$line)[0]);
				$excel[]=$row;
				$l=10;
				$row=array();
			}
		}
		if ($l>0) {
				array_unshift($row,explode(' ',$line)[0]);
				$excel[]=$row;
		}
		$xlsx = SimpleXLSXGen::fromArray( $excel );
		$xlsx->downloadAs('PlaceStats.xlsx');
	} else {
		$dir=scandir($installdir . '/names');
		foreach ($dir as $file)
			if ($file!='.' && $file!='..') 
				$names[explode('.',$file)[0]]=trim(file($installdir . '/names/' . $file)[0]);
		$excel=array();
		foreach ($names as $key=>$name) {
			$excel[]=['Data','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00',$name];
			$lines=file($installdir . '/places/' . $key . '.txt');
			$l=intval(substr(explode(' ',$lines[0])[1],0,2));
			$row=array();
			for ($i=0;$i<$l-10;$i++)
				$row[]=0;
			foreach ($lines as $line) {
				$row[]=intval(substr(explode(' ',$line)[2],0,strlen(explode(' ',$line)[2])-1));
				$l++;
				if ($l==21) {
					array_unshift($row,explode(' ',$line)[0]);
					$excel[]=$row;
					$l=10;
					$row=array();
				}
			}
			if ($l>10) {
				array_unshift($row,explode(' ',$line)[0]);
				$excel[]=$row;
			}
		}
		$xlsx = SimpleXLSXGen::fromArray( $excel );
		$xlsx->downloadAs('GlobalStats.xlsx');
}
?>
