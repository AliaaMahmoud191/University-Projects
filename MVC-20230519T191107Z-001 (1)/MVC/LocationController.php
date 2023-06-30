<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use App\Models\Location;
use Illuminate\Http\Request;

class LocationController extends Controller
{
    /*
      Display a listing of the resource.
      ., ., ., ., .,.,.,
     */
    public function index()
    {
      return Location::all();
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        $request->validate([
            'lng'               => 'required',
            'description'       => 'required',
            'lat'               => 'required',
            'userName'          => 'required',
            'userPhoneNumber'   => 'required',
        ]);

        \Log::info($request->all()) ;

        return Location::create($request->all()) ;
    }

    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        return Location::find($id);
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, string $id)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        return Location::destroy($id);
    }
}
